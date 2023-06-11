import os

from definitions import nl, nl2, _or, TOKEN_UNCERTAINTY_BUFFER
from pack.modules.core.config_mgmt.monkey_config.monkey_config_class import MonkeyConfig
from pack.modules.core.gpt.gpt_client import GPTClient
from pack.modules.core.gpt.token_counter import TokenCounter
from pack.modules.core.tasks.check_output import check_output
from pack.modules.core.theme.theme_functions import print_t


def process_file(the_file_path, special_file_summary: str = '', m: MonkeyConfig = None):
    print(f"Processing file: {the_file_path}")

    the_file_name = os.path.basename(the_file_path)
    # the_file_name = os.path.splitext(os.path.basename(the_file_path))[0]

    # Prepare output filename
    output_filename = f"{the_file_name}{m.OUTPUT_FILENAME_APPEND}{m.OUTPUT_EXT}"

    if m.SKIP_EXISTING_OUTPUT_FILES and os.path.exists(output_filename):
        print_t(f"SKIP_EXISTING_OUTPUT_FILES is True. Skipping: {output_filename}", 'warning')
        return

    # Replace {the-file} in any PROMPT monkey config props with the filename
    m.replace_prompt_str('{the-file}', the_file_name)

    with open(the_file_path, "r") as f:
        file_contents = f.read()

    if special_file_summary != '':
        special_file_summary = f"{special_file_summary}"

    main_prompt, ultimatum, output_example =\
        (_or(m.MAIN_PROMPT), _or(m.MAIN_PROMPT_ULTIMATUM), _or(m.OUTPUT_EXAMPLE_PROMPT))

    full_prompt = f"{main_prompt}{nl}{special_file_summary}{nl}{the_file_name}:{nl}" \
                  f"```{file_contents}```{nl}{ultimatum}{nl}{output_example}"

    full_prompt_log = f"{main_prompt}{nl2}<special-file-summary-or-content>{nl2}{the_file_name}:{nl}" \
                      f"```<file contents>```{nl2}{ultimatum}{nl2}{output_example}"
    print_t(f"Full prompt:{nl}{full_prompt_log}", 'info')

    token_counter = TokenCounter(m.MAIN_MODEL)
    full_prompt_tokens = token_counter.count_tokens(full_prompt)
    remaining_tokens = m.MAX_TOKENS - full_prompt_tokens - TOKEN_UNCERTAINTY_BUFFER

    # Prepare GPT client for Main Prompt
    main_gpt_client = GPTClient(m.MAIN_MODEL, remaining_tokens, m.MAIN_TEMP)

    # Prepare output directory
    output_dir = os.path.join(m.OUTPUT_PATH)
    os.makedirs(output_dir, exist_ok=True)

    for attempt in range(1, m.OUTPUT_TRIES_LIMIT + 1):
        print_t(f"Attempt {attempt} of {m.OUTPUT_TRIES_LIMIT} to process: {the_file_name}...", 'loading')
        main_gpt_response = main_gpt_client.generate(full_prompt)

        if m.OUTPUT_REMOVE_STRINGS is not None:
            for remove_str in m.OUTPUT_REMOVE_STRINGS.split(','):
                main_gpt_response = main_gpt_response.replace(remove_str, '')

        print_t("Output returned!", 'success')
        print_t(f"{main_gpt_response}", 'file')

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