from codemonkeys.utils.monkey_config.monkey_config_validations import validate_str, validate_path, validate_int, \
    validate_float, validate_bool

INPUT_PROMPTS = [
    ('MAIN_PROMPT', validate_str,
     "Provide the main prompt of your automation. Ex: Translate the file from English to Spanish."),
    ('MAIN_PROMPT_ULTIMATUM', validate_str,
     "Clearly, forcefully, and briefly assert any criteria, constraints, etc. Ex: Always write Spanish in a Colombian "
     "dialect."),
    ('WORK_PATH', validate_path,
     "What is the working directory of your automation? Ex: ~/Documents/love-poems"),
    ('CONTEXT_FILE_PATH', validate_path,
     "Enter the path to a file to be summarized using CONTEXT_SUMMARY_PROMPT. (absolute path)"),
    ('CONTEXT_SUMMARY_PROMPT', validate_str,
     "Provide a prompt for summarizing the 'Special File'. Press enter to skip summarization or if no Special File."),
    ('MAIN_MODEL', validate_int,
     "Enter the model to use for the main prompts. Choose 3 (gpt-3.5-turbo) or 4 (gpt-4)"),
    ('SUMMARY_MODEL', validate_int,
     "Enter the model to use for the summary prompts. Choose 3 (gpt-3.5-turbo) or 4 (gpt-4)"),
    ('MAIN_TEMP', validate_float,
     "Enter the temperature to use for the main prompts (a value between 0 and 1)"),
    ('SUMMARY_TEMP', validate_float,
     "Enter the temperature to use for the summary prompts (a value between 0 and 1)"),
    ('OUTPUT_EXAMPLE_PROMPT', validate_str,
     "A direct example of how the new or updated file should be formatted, (inserted in prompt). Ex: Limit your "
     "output strictly to the contents of the translated file, like: <translated-poem>"),
    ('OUTPUT_CHECK_MODEL', validate_int,
     "Enter the model to use for the usage prompts. Choose 3 (gpt-3.5-turbo) or 4 (gpt-4)"),
    ('OUTPUT_CHECK_TEMP', validate_float,
     "Enter the temperature to use for the usage prompts (a value between 0 and 1)"),
    ('WRITE_METHOD', validate_str,
     "How should the output be written? Opts: 'new', 'overwrite', 'append', 'prepend'"),
    ('OUTPUT_PATH', validate_path,
     "Please enter a path to write output files to (absolute path) (default: WORK_PATH)"),
    ('OUTPUT_FILENAME_APPEND', validate_str,
     "Please enter text to append to output filenames"),
    ('OUTPUT_EXT', validate_str,
     "Please enter text to override output file extensions"),
]
