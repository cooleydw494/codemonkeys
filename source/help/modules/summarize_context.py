
from source.utils.monk.theme.theme_functions import print_t


def main():
    print_t("Summarize Context Module Help", "important")
    print_t("The summarize_context module is designed to process and summarize "
            "the special context file within the CodeMonkeys framework. It can "
            "be used to provide a shorter, more concise version of the context "
            "information to save space and improve readability.")

    print_t("Import the module:", "file")
    print_t("from modules.custom.summarize_context import summarize_context_file")

    print_t("Usage:", "info")
    print_t("summarize_context_file(m: MonkeyConfig, allow_unsummarized: bool = False)")

    print_t("Parameters:", "info")
    print_t("m - A MonkeyConfig object instance containing the special context "
            "file path and other relevant configuration information.")
    print_t("allow_unsummarized - If set to False, the function will raise an "
            "error if the CONTEXT_SUMMARY_PROMPT is not provided in the MonkeyConfig object.")

    print_t("Exception Handling:", "warning")
    print_t("ValueError - Raised when allow_unsummarized is set to False "
            "but CONTEXT_SUMMARY_PROMPT is not provided.")
    print_t("FileNotFoundError - Raised when the specified context file "
            "cannot be found.")
    print_t("RuntimeError - Raised when the module fails to generate a summary "
            "for the context file.")

    print_t("Examples:", "special")
    print_t("Suppose you have a MonkeyConfig object `m` containing the relevant "
            "configuration information. Use the following command to generate a summarized version of "
            "the context file:")
    print_t("context_summary = summarize_context_file(m)")

    print_t("To allow unsummarized context when no summary prompt is provided, set allow_unsummarized to True:")
    print_t("context_summary = summarize_context_file(m, allow_unsummarized=True)")

    print_t("Tip", "tip")
    print_t("This module uses the GPTClient for text summarization and splitting large "
            "context files into smaller chunks. Make sure your MonkConfig object contains the "
            "necessary configuration for GPTClient, including SUMMARY_MODEL, SUMMARY_TEMP, "
            "and MAX_TOKENS.")


if __name__ == "__main__":
    main()
