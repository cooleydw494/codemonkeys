def get_env_prop_type(env_value):
    """
    Returns the appropriate Python type for the given environment variable.
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

    # Default to string
    return 'str'
