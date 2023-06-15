
from theme_functions import (
    print_t,
    print_banner,
    print_table,
    print_tree,
    input_t,
)

def main():
    print_banner()
    print_t("Theme Functions Help", "important")
    print_t("Welcome to theme_functions, a Python module that provides a set of functions for printing beautifully formatted and themed text in the CodeMonkeys framework. This module is widely used within the Monk CLI for providing rich user experiences.")

    print_t("Available Functions:", "emphasis")

    print_t("1. print_t(text, theme, incl_prefix=True, attrs=None):", "input")
    print_t("This function prints text with the specified color theme, optional inclusion of a theme-specific prefix, and text attributes such as bold and underline.")
    print_t("For instance:", "info")
    print_t("print_t('Hello, Monk CLI!', 'success')", "code")
    print_t("This statement will print a success message indicating 'Hello, Monk CLI!'", "info")

    print_t("2. print_banner():", "input")
    print_t("This function prints a built-in banner with a custom logo.")
    print_t("For instance:", "info")
    print_t("print_banner()", "code")
    print_t("This statement will display the banner at the beginning of a script execution, typically used in the Monk CLI.", "info")

    print_t("3. print_table(table, title=None, sub_indent='   ', min_col_width=None):", "input")
    print_t("This function prints an input table in a human-readable format.")
    print_t("Example:", "info")
    print_t("print_table(USAGE_EXAMPLES_TABLE, 'Usage')", "code")
    print_t("Where USAGE_EXAMPLES_TABLE is a dictionary with keys 'headers', 'show_headers' and 'rows'.", "info")

    print_t("4. print_tree(...):", "input")
    print_t("This function prints the file and directory structure of a given directory, formatted as a tree.")
    print_t("For instance:", "info")
    print_t("print_tree(start_dir='my_folder', exclude_dirs=['.git'], exclude_file_starts=['.'], title='My Folder Content')", "code")
    print_t("This statement will display the file and directory structure of 'my_folder', excluding the '.git' directory.", "info")

    print_t("5. input_t(text, input_options=None, theme='input'):", "input")
    print_t("This function prompts the user for input, displaying a themed text message and optional input choices.")
    print_t("For instance:", "info")
    print_t("response = input_t('Enter your name:', input_options='(1-30 characters)')", "code")
    print_t("This statement will prompt the user to enter their name with an accompanying hint describing the allowed input.", "info")

    print_t("Tip: Explore the theme_functions.py module to discover more function details, themes and examples.", "tip")
    print_t("Enjoy creating beautiful CLI outputs with theme_functions in the CodeMonkeys framework!", "success")

if __name__ == "__main__":
    main()
