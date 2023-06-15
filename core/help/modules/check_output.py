
from core.utils.monk.theme.theme_functions import print_t


def main():
    print_t("Check Output Module Help", "important")
    print_t("The check_output module is a utility within the CodeMonkeys framework that validates "
            "the generated output to ensure it meets certain criteria before accepting it.")
    
    print_t("Module Usage", "info")
    
    print_t("check_output(updates: str, m: MonkeyConfig) -> bool:", "input")
    
    print_t("Parameters:", "tip")
    print_t("updates: str - The generated updates to be validated", "info")
    print_t("m: MonkeyConfig - The configuration object with required parameters", "info")
    
    print_t("Return:", "tip")
    print_t("bool: True if the output is valid, otherwise False", "info")
    
    print_t("How it works:", "warning")
    print_t("The function constructs a check_prompt using the updates and the configuration's "
            "OUTPUT_CHECK_PROMPT. It then creates a GPTClient instance and generates check_result "
            "from the check_prompt. If check_result is 'true', it returns True, indicating that the "
            "output is valid. Otherwise, it returns False, prompting a retry.", "info")
    
    print_t("Example usage:", "special")
    print_t("from modules.abilities.check_output import check_output", "file")
    print_t("from core.config_mgmt.monkey_config.monkey_config_class import MonkeyConfig", "file")
    
    print_t("m = MonkeyConfig()", "input")
    print_t("updates = '''These are some updates to be validated.'''", "input")
    print_t("is_valid = check_output(updates, m)", "input")
    print_t("if is_valid: print('Output is valid')", "input")

if __name__ == "__main__":
    main()
