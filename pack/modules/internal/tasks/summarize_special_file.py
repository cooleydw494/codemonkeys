import os

from definitions import TOKEN_UNCERTAINTY_BUFFER, nl
from pack.modules.internal.config_mgmt.monkey_config.monkey_config_class import MonkeyConfig
from pack.modules.internal.gpt.gpt_client import GPTClient
from pack.modules.internal.gpt.token_counter import TokenCounter
from pack.modules.internal.theme.theme_functions import print_t


def summarize_special_file(m: MonkeyConfig):

    special_file = os.path.expanduser(m.SPECIAL_FILE_PATH)
    if not os.path.isfile(special_file):
        raise FileNotFoundError(f"The special file {special_file} does not exist.")

    special_file_contents = ''

    if m.SPECIAL_FILE_PATH:
        with open(special_file, "r") as f:
            special_file_contents = f.read()

    if not m.SUMMARY_PROMPT:
        print_t('No summary prompt was provided. Skipping summarization.', 'quiet')
        if special_file_contents != '':
            print_t(f"Un-summarized Special File:{nl}{special_file_contents}", 'file')
            return special_file_contents
        else:
            print_t(f"No Special File", 'quiet')
        return None
    else:
        token_counter = TokenCounter(m.SUMMARY_MODEL)
        special_file_contents = token_counter.split_into_chunks(special_file_contents, m.MAX_TOKENS)

    special_file_contents = '' if special_file_contents == '' else special_file_contents

    if len(special_file_contents) > 1:
        print_t(f"Split the special file {special_file} into {len(special_file_contents)} chunks.", 'info')
        print_t('Summarizing each chunk... [see TODO in summarize_special_file.py]', 'loading')
        # TODO: implement summarization of chunked special files
        exit()

    # If not chunked (length 1), summarize the special file
    summary_prompt = f'{m.SUMMARY_PROMPT}: ```{special_file_contents[0]}```'
    summary_prompt_tokens = token_counter.count_tokens(summary_prompt)
    remaining_tokens = m.MAX_TOKENS - summary_prompt_tokens - TOKEN_UNCERTAINTY_BUFFER
    summary_client = GPTClient(m.SUMMARY_MODEL, remaining_tokens, m.SUMMARY_TEMP)
    special_file_summary = summary_client.generate(summary_prompt)

    # Check if a summary was successfully generated
    if not special_file_summary:
        raise RuntimeError(f"Failed to generate a summary for the special file {special_file}.")

    print_t("Special file summarized!", 'success')
    print_t(f"Summary:{nl}{special_file_summary}", 'file')

    return special_file_summary
