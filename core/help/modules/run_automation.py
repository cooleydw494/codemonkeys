
from core.utils.monk.theme.theme_functions import print_t


def main():
    print_t("Run Automation Help", "important")
    print_t("The run_automation.py module is used to execute automations within the CodeMonkeys framework."
            "It provides a simple, yet powerful interface to run automations by dynamically importing, "
            "instantiating, and executing classes from module files.", "info")

    print_t("Sample usage:", "input")
    print_t("To use the run_automation.py module, you can import it in another script and call the "
            "run_automation function with the appropriate arguments as shown below:", "info")
    print_t("from run_automation import run_automation", "file")
    print_t("run_automation(entity_path='/path/to/your_module.py', monk_args={...})", "file")

    print_t("Function signature:", "input")
    print_t("run_automation(entity_path: str, monk_args: dict) -> None", "file")

    print_t("Function arguments", "special")
    print_t("1. entity_path (str): A string containing the path to the Python module containing the automation", "info")
    print_t("2. monk_args (dict): A dictionary containing any additional arguments required by the automation", "info")

    print_t("How it works", "special")
    print_t("The run_automation function first normalizes the given entity path and extracts the module name."
            "It then creates a module spec and loads the module from the specified entity path. The module's "
            "class, assumed to have the same name as the module, is then instantiated and executed.", "info")

    print_t("Note: Make sure that the automation module contains a class whose name matches the module (file) name,"
            "and that the class is properly implemented to work within the CodeMonkeys framework.", 'tip')
