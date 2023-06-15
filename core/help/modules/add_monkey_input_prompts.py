from core.utils.monk.theme.theme_functions import print_t


def main():
    print_t("Add Monkey Input Prompts Help", "important")
    print_t("This module is designed to configure input prompts for automation scripts within the CodeMonkeys framework.")
    
    print_t("Module: add_monkey_input_prompts", "input")
    
    print_t("Add Monkey Input Prompts is a module that contains INPUT_PROMPTS, a list of tuples that define the prompts to receive user input for constructing and configuring automation scripts. Each tuple contains a prompt name, a validation function to validate the user's input, and a description for the prompt.", "info")

    print_t("This module provides input prompts that are commonly used in automation scripts, such as the main prompt for the automation, the model and temperature settings for GPT, and the output formatting.", "info")

    print_t("How It Works", "success")
    print_t("When an automation script requires user input, it can import INPUT_PROMPTS from this module, using: `from add_monkey_input_prompts import INPUT_PROMPTS`. Then, the script can utilize the input prompt tuple to display the prompt to the user, validate their input, or provide necessary information.", "info")

    print_t("Available Prompts in this Module", "special")
    print_t("Some of the commonly used prompts include:", "info")
    print_t("- MAIN_PROMPT: This is the main prompt of the automation", "tip")
    print_t("- MAIN_TEMP: The temperature value for the main prompts", "tip")
    print_t("- OUTPUT_CHECK_MODEL: The model to use for the output check", "tip")
    print_t("- WRITE_METHOD: The method to write output files", "tip")
    
    print_t("Adding New Input Prompts", "warning")
    print_t("To add new input prompts, simply extend the INPUT_PROMPTS list by adding a tuple with the new prompt's name, validation function and description.", "info")

    print_t("Example:", "file")
    print_t("To add a hypothetical input prompt, you may do the following:", "file")
    
    print_t("", "file")
    print_t("INPUT_PROMPTS.extend([(\"DEMO_PROMPT\", validate_str, \"This is a demo prompt example.\")])", "file")
    print_t("", "file")

    print_t("Now, the DEMO_PROMPT will be available to automation scripts alongside the other prompts from this module.", "info")

if __name__ == '__main__':
    main()