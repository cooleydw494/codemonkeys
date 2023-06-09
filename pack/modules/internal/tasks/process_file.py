import os

from pack.modules.internal.config_mgmt.monkey_config.monkey_config_class import MonkeyConfig
from pack.modules.internal.gpt.token_counter import TokenCounter
from pack.modules.internal.gpt.gpt_client import gpt_client, GPTClient
from pack.modules.internal.tasks.check_output import check_output
from pack.modules.internal.theme.theme_functions import print_t

sep = os.linesep
sep2 = sep * 2


def process_file(file_path, special_file_summary: str = '', m: MonkeyConfig = None):
    print(f"Processing file: {file_path}")

    file_to_process_name = os.path.basename(file_path)
    main_prompt = m.MAIN_PROMPT.replace('{file-to-process}', file_to_process_name)

    with open(file_path, "r") as f:
        file_contents = f.read()

    if special_file_summary != '':
        special_file_summary = f"{special_file_summary}"

    ultimatum = f"```{m.MAIN_PROMPT_ULTIMATUM.replace('{file-to-process}')}```" if m.MAIN_PROMPT_ULTIMATUM != '' else ''

    output_example = f"{m.OUTPUT_EXAMPLE.replace('{file-to-process}', file_to_process_name)}" if m.OUTPUT_EXAMPLE != '' else ''

    full_prompt = f"{main_prompt}{sep}{special_file_summary}{sep}{file_to_process_name}:{sep}" \
                  f"```{file_contents}```{ultimatum}{sep}{output_example}"

    full_prompt_log = f"{main_prompt}{sep2}{special_file_summary}{sep2}{file_to_process_name}:{os.linesep}" \
                      f"```<file contents>```{ultimatum}{sep2}{output_example}"
    print_t(f"Full prompt:{os.linesep}{full_prompt_log}", 'info')

    token_counter = TokenCounter('gpt-4')  # TODO: use correct model (counter needs to handle 3/4)
    full_prompt_tokens = token_counter.count_tokens(full_prompt)
    remaining_tokens = m.MAX_TOKENS - full_prompt_tokens - 5  # 5 is just meant to be a counting imprecision buffer

    main_gpt_client = GPTClient(m.MAIN_MODEL, remaining_tokens, m.MAIN_TEMP)

    # Prepare output directory
    output_dir = os.path.join(m.OUTPUT_PATH)
    os.makedirs(output_dir, exist_ok=True)

    for attempt in range(1, m.OUTPUT_TRIES_LIMIT + 1):
        print_t(f"Attempt {attempt} of {m.OUTPUT_TRIES_LIMIT} to process: {file_to_process_name}...", 'loading')
        main_gpt_response = main_gpt_client.generate(full_prompt)

        print_t("Output returned!", 'success')
        print_t(f"{main_gpt_response}", 'file')

        # Prepare output filename
        filename = os.path.splitext(os.path.basename(file_path))[0]
        output_filename = f"{filename}{m.OUTPUT_FILENAME_APPEND}{m.OUTPUT_EXT}"

        # Check the output
        if check_output(main_gpt_response, m):
            # Save main_gpt_response to output file
            output_file_path = os.path.join(output_dir, output_filename)
            with open(output_file_path, "w") as f:
                f.write(main_gpt_response)
            print(f"Output is valid. Updated contents saved to: {output_file_path}")
            return

    print_t(f"Failed to generate valid output in {m.OUTPUT_TRIES_LIMIT} tries. Consider revising your OUTPUT config "
            f"props or increasing OUTPUT_TRIES_LIMIT.", 'warning')
