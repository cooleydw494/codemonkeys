
from core.utils.monk.theme.theme_functions import print_t


def main():
    print_t("Get Environment Property Type Help", "important")
    print_t("The get_env_prop_type module is part of the CodeMonkeys framework, "
            "aimed at assisting developers in identifying the appropriate Python data type for a given environment variable.")

    print_t("Usage:", "input")
    print_t("from path.to.get_env_prop_type import get_env_prop_type")
    print_t("prop_type = get_env_prop_type(env_value)")

    print_t("The get_env_prop_type function takes a single argument, 'env_value', which is the value of the environment variable "
            "whose data type you want to determine. It returns a string representing the Python data type most suitable for this value.", "info")

    print_t("Supported data types include:", "info")
    print_t("- 'bool' (boolean) for values 'true' and 'false'")
    print_t("- 'List[str]' (list of strings) for comma-separated values")
    print_t("- 'int' (integer) for numeric values without decimals")
    print_t("- 'float' (floating-point number) for numeric values with decimals")
    print_t("- 'str' (string) as a default for any other value")

    print_t("Examples:", "special")
    print_t("> get_env_prop_type('true') -> 'bool'")
    print_t("> get_env_prop_type('1,2,3') -> 'List[str]'")
    print_t("> get_env_prop_type('42') -> 'int'")
    print_t("> get_env_prop_type('3.14') -> 'float'")
    print_t("> get_env_prop_type('hello') -> 'str'")
