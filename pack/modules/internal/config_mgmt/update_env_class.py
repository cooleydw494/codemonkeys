import os

from definitions import ENV_CLASS_PATH
from pack.modules.internal.config_mgmt.env_class import required_env_props, ENV_DEFINITION_TEMPLATE, ENV_PATTERN
from pack.modules.internal.config_mgmt.env_helpers import get_env_prop_type


def update_env_class():
    """
    Updates the env_class.py file to include all environment variables as attributes of the ENV class.
    """
    # Read the current contents of the file
    with open(ENV_CLASS_PATH, "r") as f:
        content = f.read()

    # Get all environment variables and generate corresponding class definitions
    env_definitions = []
    for key, value in os.environ.items():
        if key not in required_env_props:
            env_definitions.append(ENV_DEFINITION_TEMPLATE.format(var_name=key, var_type=get_env_prop_type(value)))

    # Replace placeholder in class definition with generated definitions
    new_content = ENV_PATTERN.sub(
        "# [DEFINE_GENERATED_START]\n" + "\n".join(env_definitions) + "\n# [DEFINE_GENERATED_END]",
        content)

    # Write updated contents
    with open(ENV_CLASS_PATH, "w") as f:
        f.write(new_content)
