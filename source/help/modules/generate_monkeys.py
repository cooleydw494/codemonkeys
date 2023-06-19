from source.utils.monk.theme.theme_functions import print_t

def main():
    print_t("Generate Monkeys Help", "important")
    print_t("The 'generate_monkeys' module is an integral part of the CodeMonkeys framework, which is used to create, modify, and remove AI monkeys based on the defined manifest.")

    print_t("generate_monkeys.py", "input")

    print_t("This script reads the monkey-manifest.yaml file, applies the default configurations, and validates the manifest configurations.", "info")
    print_t("It creates or updates the configuration files for each monkey in the MONKEYS_PATH directory, and removes any previously existing monkeys that are no longer in the manifest.", "info")
    print_t("Additionally, it maintains a history of previous configurations in the .history directory within the MONKEYS_PATH.", "info")

    print_t("Usage Example:", "special")
    print_t("To use the 'generate_monkeys' module within the CodeMonkeys framework, simply import the 'generate_monkeys' module and call the 'generate_monkeys()' function.", "info")

    print_t("", "file")
    print_t("from generate_monkeys import generate_monkeys", "file")
    print_t("generate_monkeys()", "file")
    print_t("", "file")

    print_t("This will generate the AI monkeys based on the manifest configurations, and maintain a history of any changes made to the monkeys.", "info")