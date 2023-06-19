
from source.utils.monk.theme.theme_functions import print_t

def main():
    print_t("Automation Class Help", "important")
    print_t("automation_class.py module is a source component of the CodeMonkeys framework.", "info")
    print_t("It provides a base class 'Automation' to create and manage automations using the Monk CLI.", "info")
    
    print_t("Key Features:", "special")
    print_t("1. Automatically performs environment checks.", "success")
    print_t("2. Handles the loading and validation of Monkey configuration files.", "success")
    print_t("3. Implements methods to initialize File List Manager.", "success")
    print_t("To create a new automation, subclass the 'Automation' class and implement its 'main()' method.", "tip")
    
    print_t("Example Usage:", "special")
    print_t("from automation_class import Automation", "file")
    print_t("class MyAutomation(Automation):", "file")
    print_t("    def main(self):", "file")
    print_t("        # Custom automation logic", "file")
    
    print_t("An instance of 'MyAutomation' class can be initialized with 'monk_args' (parsed command line arguments).", "info")
    print_t("After initialization, the 'main()' method can be called to run the custom automation logic.", "info")

    print_t("Remember to add any configuration keys required by your automation to 'required_config_keys'.", "warning")
    print_t("This will help ensure your automation has the necessary configurations before execution.", "warning")

main()
