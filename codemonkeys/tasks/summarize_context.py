import os

from defs import import_monkey_config_class
from defs import nl
from codemonkeys.utils.monk.theme_functions import print_t
from codemonkeys.abilities.gpt_client import GPTClient

MonkeyConfig = import_monkey_config_class()


def summarize_context_file(m: MonkeyConfig, allow_unsummarized: bool = False):

    if allow_unsummarized is False and m.CONTEXT_SUMMARY_PROMPT is None:
        raise ValueError("CONTEXT_SUMMARY_PROMPT is None, but allow_unsummarized is False.")

    context_file = os.path.expanduser(m.CONTEXT_FILE_PATH)
    if not os.path.isfile(context_file):
        raise FileNotFoundError(f"The context file {context_file} does not exist.")

    context_file_contents = ''

    if m.CONTEXT_FILE_PATH:
        with open(context_file, "r") as f:
            context_file_contents = f.read()

    if not m.CONTEXT_SUMMARY_PROMPT:
        print_t('No summary prompt was provided. Skipping summarization.', 'quiet')
        if context_file_contents != '':
            print_t(f"Un-summarized Special File:{nl}{context_file_contents}", 'file')
            return context_file_contents
        else:
            print_t(f"No Special File", 'quiet')
        return None
    else:
        summary_client = GPTClient(m.SUMMARY_MODEL, m.SUMMARY_TEMP, m.MAX_TOKENS)
        context_file_contents = summary_client.split_into_chunks(context_file_contents, m.MAX_TOKENS)

    context_file_contents = '' if context_file_contents == '' else context_file_contents

    if len(context_file_contents) > 1:
        print_t(f"Split the context file {context_file} into {len(context_file_contents)} chunks.", 'info')
        print_t('Summarizing each chunk... [see TODO in summarize_context.py]', 'loading')
        # TODO: implement summarization of chunked context files
        exit()

    # If not chunked (length 1), summarize the context file
    summary_prompt = f'{m.CONTEXT_SUMMARY_PROMPT}: ```{context_file_contents[0]}```'
    context_file_summary = summary_client.generate(summary_prompt)

    # Check if a summary was successfully generated
    if not context_file_summary:
        raise RuntimeError(f"Failed to generate a summary for the context file {context_file}.")

    print_t("Special file summarized!", 'success')
    print_t(f"Summary:{nl}{context_file_summary}", 'file')

    return context_file_summary
