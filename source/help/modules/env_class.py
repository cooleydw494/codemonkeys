
from source.utils.monk.theme.theme_functions import print_t

def main():
    print_t("env_class.py Help", "important")
    print_t("This module provides the ENV class, which contains environment variable definitions used within the "
            "CodeMonkeys framework. The variables are loaded from a .env file at the project's root directory, and "
            "any undefined variables will default to values specified in the class definition or from the file "
            "`stor/source/defaults/monkey-config_mgmt-defaults.yaml`.", "info")

    print_t("Key features:", "info")
    print_t("- Store required and custom environment variables in a single location.", "special")
    print_t("- Quickly access environment variables by importing and referencing the ENV class.", "special")
    print_t("- Provides a simple way to manage credentials and API keys for various services and automations.", "special")

    print_t("Importing and using environment variables in your code:", "tip")
    print_t("Simply import the ENV class from the env_class.py module and reference the desired property for the "
            "variable value.")
    print_t("Example:", "input")
    print_t("from env_class import ENV")
    print_t("print(ENV.OPENAI_API_KEY)")

    print_t("Custom environment variables:", "info")
    print_t("Define your own environment variables in your .env file, and they will be automatically recognized and "
            "added as class properties by the env_class.py module.")
    print_t("To access custom variables, simply import the ENV class and reference the desired property.", "special")
