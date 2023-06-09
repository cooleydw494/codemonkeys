import os

from pack.modules.internal.config_mgmt.monkey_config.monkey_config_class import MonkeyConfig
from pack.modules.internal.gpt.token_counter import TokenCounter
from pack.modules.internal.gpt.gpt_client import gpt_client, GPTClient
from pack.modules.internal.theme.theme_functions import print_t

sep2 = os.linesep + os.linesep


def process_file(file_path, special_file_summary: str = '', m: MonkeyConfig = None):
    print(f"Processing file: {file_path}")

    with open(file_path, "r") as f:
        file_contents = f.read()

    if special_file_summary != '':
        special_file_summary = f"{special_file_summary}"

    ultimatum = f"```{m.MAIN_PROMPT_ULTIMATUM}```" if m.MAIN_PROMPT_ULTIMATUM != '' else ''

    full_prompt = f"{m.MAIN_PROMPT}{sep2}{special_file_summary}{sep2}FILE TO PROCESS:{os.linesep}```{file_contents}```{ultimatum}"

    token_counter = TokenCounter('gpt-4')  # TODO: use correct model (counter needs to handle 3/4)
    full_prompt_tokens = token_counter.count_tokens(full_prompt)
    remaining_tokens = m.MAX_TOKENS - full_prompt_tokens - 5  # 5 is just meant to be a counting imprecision buffer

    main_gpt_client = GPTClient(m.MAIN_MODEL, remaining_tokens, m.MAIN_TEMP)

    # Prepare output directory
    output_dir = os.path.join(m.OUTPUT_PATH)
    os.makedirs(output_dir, exist_ok=True)

    for attempt in range(1, m.OUTPUT_TRIES_LIMIT + 1):
        print(f"Attempt {attempt} of {m.OUTPUT_TRIES_LIMIT} to process the file")
        main_gpt_response = main_gpt_client.generate(full_prompt)

        print_t("Output returned!", 'success')
        print_t(f"Output:{os.linesep}{main_gpt_response}", 'file')

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

    print(
        f"Failed to generate valid output after {m.OUTPUT_TRIES_LIMIT} tries. Check the input file and the MAIN_PROMPT.")


def check_output(updates: str, m: MonkeyConfig) -> bool:
    check_prompt = f"{m.OUTPUT_CHECK_PROMPT}{sep2}{updates}"
    print_t(f"Checking output with prompt:{os.linesep}{m.OUTPUT_CHECK_PROMPT}", 'file')
    check_prompt_tokens = TokenCounter('gpt-4').count_tokens(check_prompt)
    remaining_tokens = m.MAX_TOKENS - check_prompt_tokens - 5  # 5 is just meant to be a counting imprecision buffer
    check_output_gpt_client = GPTClient(m.OUTPUT_CHECK_MODEL, remaining_tokens, m.OUTPUT_CHECK_TEMP)
    check_result = check_output_gpt_client.generate(check_prompt)
    print_t(f"Output check result:{os.linesep}{check_result}", 'file')

    if check_result.lower() == 'true':
        return True
    else:
        print("Output did not pass the check. Retrying...")
        return False
