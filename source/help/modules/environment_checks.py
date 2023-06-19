
from source.utils.monk.theme.theme_functions import print_t

def main():
    print_t("Environment Checks Module Help", "important")
    print_t("The environment_checks.py module is a part of the CodeMonkeys framework, "
            "a powerful AI-ready automations system managed by the Monk CLI.")

    print_t("This module contains various functions to ensure the proper functioning "
            "of the CodeMonkeys framework within its required environment.", "info")

    print_t("Functions included in environment_checks.py:", "special")
    print_t("- monk_env_checks() \n  * Ensures Python 3 is being used, and exits with an error if not.", "info")
    print_t("- automation_env_checks() \n  * Validates the OpenAI API key and checks for connection issues.", "info")

    print_t("These functions are automatically called by various parts of the CodeMonkeys "
            "framework to ensure the environment satisfies the necessary requirements "
            "before carrying out different tasks.", "tip")
    print_t("Usage of the module functions is internal to the system and not typically "
            "required to be used by the user in custom scripts.", "warning")

main()
