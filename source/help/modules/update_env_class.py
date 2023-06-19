
from source.utils.monk.theme.theme_functions import print_t

def main():
    print_t("Update Env Class Help", "important")
    print_t("The update_env_class module allows you to update the env_class.py file to include all environment"
            " variables as attributes of the ENV class. It automatically reads and converts .env and .env.default"
            " file variables into attribute definitions within the ENV class.", "info")

    print_t("How it works:", "special")
    print_t("1. Retrieves the variables from .env and .env.default files.", "info")
    print_t("2. Reads the current contents of env_class.py and looks for markers to define attributes.", "info")
    print_t("3. Generates class definitions for both environment variables and framework environment variables.", "info")
    print_t("4. Updates the env_class.py file with the generated definitions and writes them in the appropriate locations.", "info")

    print_t("Usage:", "special")
    print_t("To use the update_env_class module, simply import the update_env_class function and call it.", "info")
    print_t("Example:", "input")
    print_t("from config.operations.update_env_class import update_env_class", "file")
    print_t("update_env_class()", "file")

main()
