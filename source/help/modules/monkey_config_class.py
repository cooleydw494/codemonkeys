from source.utils.monk.theme.theme_functions import print_t

def main():
    print_t("Monkey Config Class Help", "important")
    print_t("The monkey_config_class module provides a highly-configurable class for customized AI-driven automation workflows in the CodeMonkeys framework. This module is integrated into the Monk CLI, allowing granular customization of various properties and behavior through user-specified configurations.")

    print_t("Usage of MonkeyConfig class in automation development is essential for harnessing specific configuration properties that drive your AI automations. It offers built-in validation and default value handling for the input configuration, thus ensuring the proper setup of your workflows.", "info")

    print_t("The MonkeyConfig class centralizes the reading and handling of various configuration properties for efficient management, such as customization of included/excluded file types, handling of context summary prompts, output verification controls, and temperature settings.", "tip")

    print_t("To use the MonkeyConfig class, import and load a specific MonkeyConfig instance based on the monkey_name (automation configuration) you are using. For example, to import and load MonkeyConfig for a specific automation:", "input")
    print_t("from monkey_config_class import MonkeyConfig", "file")
    print_t("config = MonkeyConfig.load('my_custom_automation')", "file")

    print_t("With the loaded MonkeyConfig instance, you can access and utilize any of its available configurable properties, such as config.MAX_TOKENS, config.MAIN_PROMPT, etc.", "info")

    print_t("Additionally, the MonkeyConfig class provides various helper methods to filter, validate, and apply property defaults to a given configuration dictionary, allowing for seamless integration into your custom automations.", "special")

    print_t("For in-depth understanding, refer to the comments and implementation details in the monkey_config_class.py module.", "info")

main()