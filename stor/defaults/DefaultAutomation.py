import argparse

from codemonkeys.base_entitiies.automation_class import Automation
from codemonkeys.utils.monk.theme_functions import print_t
from codemonkeys.tasks.process_file import process_file
from codemonkeys.tasks.summarize_context import summarize_context_file


class Default(Automation):
    required_config_keys = ['WORK_PATH', 'MAIN_PROMPT', 'OUTPUT_EXT']

    def __init__(self, monk_args: argparse.Namespace):
        super().__init__(monk_args)

    def main(self):

        m = self.monkey_config

        context_file_summary = summarize_context_file(m, allow_unsummarized=True)

        self.flm.write_files_to_process()

        while True:
            selected_file = self.flm.select_and_remove_file()

            if selected_file is None:
                print_t("All files have been processed.", 'done')
                break

            process_file(selected_file, context_file_summary, m)
