
from core.utils.monk.theme.theme_functions import print_t

def main():
    print_t("Automation Class Help", "important")
    print_t("The automation_class.py module serves as a base class for implementing automations in the CodeMonkeys framework. It provides essential methods and functionality for running specific automations using Monk CLI.")

    print_t("Key Components of Automation Class:", "info")
    print_t("- automation_env_checks(): Ensures that the necessary environment is set up correctly before running an automation.", "list")
    print_t("- load_config(): Loads the Monkey Config file for the specific automation.", "list")
    print_t("- validate_config(): Validates that required configuration keys are present in the Monkey Config file.", "list")
    print_t("- FileListManager: Contains methods for managing file operations.", "list")
    print_t("- main(): A method that must be implemented in subclasses of Automation to define the specific automation's functionality.", "list")

    print_t("How to use the Automation Class:", "tip")
    print_t("1. Import the base Automation class from automation_class.py.", "list")
    print_t("2. Create a new subclass of Automation, and define the required_config_keys list if necessary.", "list")
    print_t("3. Override the init() method if necessary, and make sure to call the parent init().", "list")
    print_t("4. Implement the main() method, which will contain the specific functionality for your automation.", "list")
    print_t("5. Use the obtained configuration parameters and file list manager for automating tasks in the main method.", "list")

    print_t("Once the subclass has been properly implemented, you can use the Monk CLI to run your automation by passing the appropriate flags, such as '-a <your-automation-name>'.", "special")

main()
