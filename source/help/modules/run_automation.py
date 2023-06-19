
from source.utils.monk.theme.theme_functions import print_t

def main():
    print_t("Run Automation Module Help", "important")
    print_t("The run_automation.py module is used to execute automations within the CodeMonkeys framework."
            "Its purpose is to import, instantiate, and run a specified automation by providing the entity path"
            "and Monk command line arguments.")
    
    print_t("Usage:", "special")
    print_t("import run_automation")
    print_t("run_automation.run_automation(entity_path, monk_args)")

    print_t("Parameters:", "special")
    print_t("- entity_path: Path to the automation file.", "info")
    print_t("- monk_args: List of command line arguments for Monk CLI.", "info")

    print_t("Example:", "special")
    print_t("Suppose we have an automation named 'my_automation.py' in the '/path/to/automations' folder.", "info")
    print_t("To run 'my_automation.py' with the Monk command line arguments ['-f', 'input.txt'], you may use the following code:", "info")

    print_t("import run_automation", "input")
    print_t("entity_path = '/path/to/automations/my_automation.py'", "input")
    print_t("monk_args = ['-f', 'input.txt']", "input")
    print_t("run_automation.run_automation(entity_path, monk_args)", "input")

    print_t("The run_automation.py module functions will import 'my_automation.py',"
            "instantiate the class with the provided command line arguments, and execute its main() method.", "tip")
