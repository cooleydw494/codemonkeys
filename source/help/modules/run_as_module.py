
from source.utils.monk.theme.theme_functions import print_t

def main():
    print_t("Run as Module Help", "important")
    print_t("This script provides a helper function 'run_as_module' to run another Python module within the "
            "CodeMonkeys framework with optional monk_args. It also manages the extraction and execution of "
            "the main function within the target module.")

    print_t("Function Signature:", "info")
    print_t("run_as_module(module_path, function_name='main', monk_args=None)", "input")

    print_t("Parameters Explanation:", "tip")
    print_t("- module_path: The path of the module you want to run", "info")
    print_t("- function_name: The name of the main function you want to run in the module (default is 'main')", "info")
    print_t("- monk_args: Any arguments you want to pass to the main function (default is None)", "info")

    print_t("Example Usage:", "special")
    print_t("run_as_module('example_module.py', 'main', {'key': 'value'})", "file")

    print_t("Important Notes:", "warning")
    print_t("1. The main function within the target module should take either one argument (monk_args) or no arguments."
            "If your main function takes more than one argument, you may need to modify 'run_as_module.py'.", "info")
    print_t("2. Always use 'run_as_module' function when running another module within the CodeMonkeys framework. "
            "This will ensure proper management and execution of the target module's main function.", "info")

main()
