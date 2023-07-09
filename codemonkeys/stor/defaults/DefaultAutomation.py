import argparse
from typing import Dict, Any, List

from codemonkeys.abilities.file_list_manager import FileListManager
from codemonkeys.base_entitiies.automation_class import Automation
from codemonkeys.utils.monk.theme_functions import print_t
from codemonkeys.tasks.process_file import process_file
from codemonkeys.tasks.context_summarizer import ContextSummarizer


class Default(Automation):
    required_config_keys = ['WORK_PATH', 'MAIN_PROMPT', 'OUTPUT_EXT']

    def __init__(self, monk_args: argparse.Namespace, named_args: Dict[str, Any], unnamed_args: List[str]):
        super().__init__(monk_args, named_args, unnamed_args)

        self.file_list_manager = FileListManager()

    def run(self):

        m = self.monkey_config

        context_file_summary = (ContextSummarizer()
                                .allow_unsummarized()
                                .set_prompt(m.SUMMARY_PROMPT)
                                .context_file(m.CONTEXT_FILE_PATH)
                                .set_model(m.SUMMARY_MODEL, m.SUMMARY_TEMP, m.MAX_TOKENS)
                                .summarize())

        file_list_manager = (FileListManager()
                             .set_file_types_included(m.FILE_TYPES_INCLUDED)
                             .set_filepath_match_excluded(m.FILEPATH_MATCH_EXCLUDED)
                             .set_filter_max_tokens(m.FILE_SELECT_MAX_TOKENS)
                             .set_token_count_model(m.MAIN_MODEL)
                             .set_work_path(m.WORK_PATH)
                             .set_output_file('files-to-process.txt'))

        while True:
            selected_file = file_list_manager.pop_file()

            if selected_file is None:
                print_t("All files have been processed.", 'done')
                break

            process_file(selected_file, context_file_summary, m)
