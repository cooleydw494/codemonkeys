import argparse
from typing import Dict, Any, List

from codemonkeys.composables.file_iterator import FileIterator
from codemonkeys.base_entities.automation_class import Automation
from codemonkeys.composables.output_checker import OutputChecker
from codemonkeys.composables.output_path_resolver import OutputPathResolver
from codemonkeys.utils.monk.theme_functions import print_t
from codemonkeys.composables.file_handler import FileHandler
from codemonkeys.composables.context_summarizer import ContextHandler


class Default(Automation):
    required_config_keys = ['MAIN_PROMPT']

    required_config_keys_if = {
        'OUTPUT_CHECK_PROMPT': ['OUTPUT_TRIES'],
    }

    def __init__(self, monk_args: argparse.Namespace, named_args: Dict[str, Any], unnamed_args: List[str]):
        super().__init__(monk_args, named_args, unnamed_args)

    def run(self):
        mc = self.monkey_config

        # Prepare summarized or unsummarized context
        if mc.CONTEXT_FILE_PATH is None:
            context = None
        else:
            context_handler = ContextHandler().context_file(mc.CONTEXT_FILE_PATH)
            if mc.SUMMARY_PROMPT:
                context = (context_handler
                           .set_model(mc.SUMMARY_MODEL, mc.SUMMARY_TEMP, mc.MAX_TOKENS)
                           .set_prompt(mc.SUMMARY_PROMPT)
                           .summarize())
            else:
                context = context_handler.get_unsummarized_context()

        # Prepare Output Checker
        output_checker = None
        if mc.OUTPUT_CHECK_PROMPT is not None:
            output_checker = (OutputChecker()
                              .set_model(mc.OUTPUT_CHECK_MODEL, mc.OUTPUT_CHECK_TEMP, mc.MAX_TOKENS)
                              .set_tries(mc.OUTPUT_TRIES)
                              .set_prompt(mc.OUTPUT_CHECK_PROMPT))

        # Prepare FileIterator and filter files
        file_iterator = (FileIterator()
                         .set_token_count_model(mc.MAIN_MODEL, mc.MAIN_TEMP, mc.MAX_TOKENS)
                         .set_file_types_included(mc.FILE_TYPES_INCLUDED)
                         .set_filepath_match_exclude(mc.FILEPATH_MATCH_EXCLUDE)
                         .set_work_path(mc.WORK_PATH)
                         .filter_files())

        output_path_resolver = (OutputPathResolver()
                                .set_output_path(mc.OUTPUT_PATH)
                                .set_output_filename_append(mc.OUTPUT_FILENAME_APPEND)
                                .set_output_ext(mc.OUTPUT_EXT))

        # Iterate through filtered files
        while True:
            current_file = file_iterator.pop_file()

            if current_file is None:
                print_t("All Files Handled.", 'done')
                break

            # Handle current file,
            (FileHandler()
             .set_model(mc.MAIN_MODEL, mc.MAIN_TEMP, mc.MAX_TOKENS)
             .set_path(current_file)
             .set_main_prompt(mc.MAIN_PROMPT)
             .set_context(context)
             .set_output_example_prompt(mc.OUTPUT_EXAMPLE_PROMPT)
             .set_ultimatum_prompt(mc.MAIN_PROMPT_ULTIMATUM)
             .set_skip_existing(mc.SKIP_EXISTING_OUTPUT_FILES)
             .set_output_checker(output_checker)
             .set_output_path_resolver(output_path_resolver)
             .handle())
