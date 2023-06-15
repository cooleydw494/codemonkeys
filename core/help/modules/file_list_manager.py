
from core.utils.monk.theme.theme_functions import print_t

def main():
    print_t("File List Manager Help", "important")
    print_t("The FileListManager module manages and filters file lists to help you select suitable files for processing "
            "within the CodeMonkeys framework. This module is especially helpful when working with a large number of "
            "files and you need to find candidates based on specific criteria.")

    print_t("Usage", "input")
    print_t("1. Import FileListManager:\n"
            "from modules.file_list_manager import FileListManager", 'code')
    print_t("2. Initialize the FileListManager with a MonkeyConfig instance:\n"
            "file_list_manager = FileListManager(monkey_config)", "code")
    print_t("3. Get a list of filtered files:\n"
            "filtered_files = file_list_manager.get_filtered_files()", 'code')
    print_t("4. Write the filtered file list to an output file:\n"
            "file_list_manager.write_files_to_process(filtered_files)", 'code')
    print_t("5. Select and remove a file from the file list:\n"
            "selected_file = file_list_manager.select_and_remove_file()", 'code')

    print_t("Customization and Configuration", "special")
    print_t("You can customize the file filtering behavior by editing the following configurations in the MonkeyConfig instance:\n"
            "  - FILE_TYPES_INCLUDED : File extensions to include\n"
            "  - FILEPATH_MATCH_EXCLUDED : Exclude files based on patterns in their path\n"
            "  - FILE_SELECT_MAX_TOKENS : Maximum allowed tokens in a file", "info")

    print_t("Example", "tip")
    print_t("Suppose you have a MonkeyConfig with the following specifications:\n"
            "  - WORK_PATH = /my_project\n"
            "  - FILE_TYPES_INCLUDED = .txt,.md\n"
            "  - FILEPATH_MATCH_EXCLUDED = _archive,backup\n"
            "  - FILE_SELECT_MAX_TOKENS = 1000\n\n"
            
            "The FileListManager will only return .txt and .md files within the /my_project directory "
            "that do not have '_archive' or 'backup' in their path and have 1000 tokens or fewer. "
            "This filtered list of files will be written to an output file with the write_files_to_process function. "
            "You can then select and remove files from the list for further processing using the select_and_remove_file function.", "info")

if __name__ == "__main__":
    main()
