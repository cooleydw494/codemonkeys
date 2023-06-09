import os

from pack.modules.internal.config_mgmt.monkey_config.monkey_config_class import MonkeyConfig
from pack.modules.internal.gpt.gpt_clients import GPTClient
from pack.modules.internal.gpt.token_counter import TokenCounter
from pack.modules.internal.theme.theme_functions import print_t


def summarize_special_file(m: MonkeyConfig):
    summary_client = GPTClient(m.SUMMARY_MODEL, m.FILE_SELECT_MAX_TOKENS, m.SUMMARY_TEMP)
    special_file = os.path.expanduser(m.SPECIAL_FILE_PATH)
    if not os.path.isfile(special_file):
        raise FileNotFoundError(f"The special file {special_file} does not exist.")

    with open(special_file, "r") as f:
        special_file_contents = f.read()

    token_counter = TokenCounter('gpt-4')
    special_file_contents = token_counter.split_into_chunks(special_file_contents, m.FILE_SELECT_MAX_TOKENS)

    if len(special_file_contents) > 1:
        print_t(f"Split the special file {special_file} into {len(special_file_contents)} chunks.", 'info')
        print_t('Summarizing each chunk...', 'loading')
        # TODO: implement summarization of chunked special files
        print_t('Just kidding, this still needs to be implemented.', 'error')
        exit()

    # If not chunked (length 1), summarize the special file
    full_prompt = f'{m.SUMMARY_PROMPT}: ```{special_file_contents[0]}```'
    special_file_summary = summary_client.generate(full_prompt)

    # Check if a summary was successfully generated
    if not special_file_summary:
        raise RuntimeError(f"Failed to generate a summary for the special file {special_file}.")

    return special_file_summary
