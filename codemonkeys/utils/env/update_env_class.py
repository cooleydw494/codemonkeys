import os
import re

from dotenv import dotenv_values

from defs import ENV_CLASS_PATH, ROOT_PATH, nl, ENV_DEFAULT_PATH
from codemonkeys.utils.env.get_env_prop_type import get_env_prop_type

ENV_DEFINITION_TEMPLATE = "    {var_name}: {var_type} = os.getenv('{var_name}')"
ENV_DEFINITION_TEMPLATE_DEFAULT = "    {var_name}: {var_type} = os.getenv('{var_name}', '{default}')"


def update_env_class():
    """
    Updates the env_class.py file to include all environment variables as attributes of the ENV class.
    """
    # Get the .env file variables
    env_vars = dotenv_values(os.path.join(ROOT_PATH, ".env"))

    # Get the .env.default file variables (codemonkeys env props)
    framework_env_vars = dotenv_values(ENV_DEFAULT_PATH)

    # Read the current contents of the file
    with open(ENV_CLASS_PATH, "r") as f:
        content_lines = f.readlines()

    required_start_marker_re = re.compile(r'\[\s*DEFINE_FRAMEWORK_ENV_PROPS_LIST_START\s*\]')
    required_end_marker_re = re.compile(r'\[\s*DEFINE_FRAMEWORK_ENV_PROPS_LIST_END\s*\]')
    framework_start_marker_re = re.compile(r'\[\s*DEFINE_FRAMEWORK_ENV_PROPS_START\s*\]')
    framework_end_marker_re = re.compile(r'\[\s*DEFINE_FRAMEWORK_ENV_PROPS_END\s*\]')
    start_marker_re = re.compile(r'\[\s*DEFINE_CUSTOM_ENV_PROPS_START\s*\]')
    end_marker_re = re.compile(r'\[\s*DEFINE_CUSTOM_ENV_PROPS_END\s*\]')

    required_start_index = required_end_index = framework_start_index = framework_end_index = start_index = end_index\
        = None

    for i, line in enumerate(content_lines):
        if required_start_marker_re.search(line):
            required_start_index = i + 1
        elif required_end_marker_re.search(line):
            required_end_index = i
        elif framework_start_marker_re.search(line):
            framework_start_index = i + 1
        elif framework_end_marker_re.search(line):
            framework_end_index = i
        elif start_marker_re.search(line):
            start_index = i + 1
        elif end_marker_re.search(line):
            end_index = i

    if None in [required_start_index, required_end_index, framework_start_index, framework_end_index, start_index,
                end_index]:
        raise Exception("Couldn't find all markers in the class file.")

    # Get all environment variables and generate corresponding class definitions
    env_definitions = []
    for key, value in env_vars.items():
        if key not in framework_env_vars.keys():
            env_definitions.append(ENV_DEFINITION_TEMPLATE.format(var_name=key, var_type=get_env_prop_type(value)))

    # Get codemonkeys environment variables and generate corresponding class definitions
    framework_env_definitions = []
    for key, value in framework_env_vars.items():
        var_type = get_env_prop_type(value)
        framework_env_definitions.append(
            ENV_DEFINITION_TEMPLATE_DEFAULT.format(var_name=key, var_type=var_type, default=value))

    # Generate the required env props list
    required_env_props_list = ', '.join(['"' + key + '"' for key in framework_env_vars.keys()])
    required_env_props_def = f"required_env_props = [{required_env_props_list}]"

    # Replace placeholder in class definition with generated definitions
    new_content_lines = content_lines[:required_start_index] + [required_env_props_def, nl] + \
                            content_lines[required_end_index:framework_start_index] + [
                            line + nl for line in framework_env_definitions] + [nl] + \
                            content_lines[framework_end_index:start_index] + [
                            line + nl for line in env_definitions] + [nl] + content_lines[end_index:]

    # Write updated contents
    with open(ENV_CLASS_PATH, "w") as f:
        f.writelines(new_content_lines)
