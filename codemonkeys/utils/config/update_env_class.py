import importlib
import os
import re
from typing import List

from dotenv import dotenv_values

from codemonkeys.defs import ENV_CLASS_PATH, ROOT_PATH, nl
from codemonkeys.utils.misc.handle_exception import handle_exception
from codemonkeys.utils.monk.theme_functions import print_t

try:
    # import this in a non-standard way to allow force-reloading the module
    import config.env
    Env = config.env.Env
except ImportError as e:
    print_t('Could not import user Env class from config.env. Using default Env class.', 'warning')
    handle_exception(e, always_continue=True)
    from codemonkeys.config.env import Env

ENV_DEFINITION_TEMPLATE = "    {var_name}: {var_type} = os.getenv('{var_name}')"
ENV_DEFINITION_TEMPLATE_DEFAULT = "    {var_name}: {var_type} = os.getenv('{var_name}', '{default}')"


def force_reload_env_class() -> None:
    """
    Force reload of the user Env class.

    This function attempts to reload the custom user-defined Env class from
    the config.env module.
    """
    try:
        importlib.reload(config.env)
    except ImportError as e:
        print_t('Could not import user Env class from config.env. Using default Env class.',
                'warning')
        handle_exception(e, always_continue=True)


def get_env_prop_type(env_value: str) -> str:
    """
    Determine the Python type for a given environment variable value.

    This function reads the value of the environment variable and determines
    its corresponding Python type. It recognizes booleans, integers, floats, lists,
    and defaults to a string type if none of the specific types match.

    :param env_value: The value of the environment variable.
    :type env_value: str
    :return: The Python type as a string.
    :rtype: str
    """
    # Check for boolean
    if env_value.lower() in ('true', 'false'):
        return 'bool'

    # Check for list, comma separated values
    elif ',' in env_value:
        return 'List[str]'

    # Check for integer
    if env_value.isdigit():
        return 'int'

    # Check for float
    if '.' in env_value and env_value.replace('.', '', 1).isdigit():
        try:
            float(env_value)
            return 'float'
        except ValueError:
            pass

    # Default to str
    return 'str'


def update_env_class() -> None:
    """
    Update the Env class with properties defined in the .env file.

    This function reads the .env file at the project's root and dynamically
    generates type-hinted properties in the Env class to match defined environment
    variables. It uses markers within the Env class file to identify the insertion
    points for generated code.

    :raises Exception: If start or stop markers for env prop definitions are missing.
    """
    # Get the .env file variables
    env_vars = dotenv_values(os.path.join(ROOT_PATH, ".env"))

    # Read the current contents of the file
    with open(ENV_CLASS_PATH, "r") as f:
        content_lines = f.readlines()

    start_marker_re = re.compile(r'\[\s*DEFINE_ENV_PROPS_START\s*\]')
    end_marker_re = re.compile(r'\[\s*DEFINE_ENV_PROPS_END\s*\]')

    start_index = end_index = None

    for i, line in enumerate(content_lines):
        if start_marker_re.search(line):
            start_index = i + 1
        elif end_marker_re.search(line):
            end_index = i

    if None in [start_index, end_index]:
        raise Exception("Couldn't find env prop start/stop markers in the Env class.")

    # Get all environment variables and generate corresponding class definitions
    env_definitions: List[str] = []
    for key, value in env_vars.items():
        env_definitions.append(ENV_DEFINITION_TEMPLATE.format(var_name=key, var_type=get_env_prop_type(value)))

    # Replace placeholder in class definition with generated definitions
    new_content_lines = (
            content_lines[:start_index]
            + [line + nl for line in env_definitions]
            + content_lines[end_index:]
    )

    # Write updated contents
    with open(ENV_CLASS_PATH, "w") as f:
        f.writelines(new_content_lines)
