import importlib
import inspect

from codemonkeys.utils.monk.theme_functions import print_t


# This function is important for maintaining the pack "pseudo-package" paradigm.
def run_as_module(module_path, function_name='main', monk_args=None):
    spec = importlib.util.spec_from_file_location('module', module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    if hasattr(module, function_name):
        function = getattr(module, function_name)
        args_count = len(inspect.getfullargspec(function).args)

        # Default Behavior:
        # Assuming the function takes args, namely the codemonkeys-intended monk_args
        # (ex: add-monkey.py@main)
        if args_count == 1:
            return function(monk_args)

        # If the function takes no args, just run it. This should work IMO, but codemonkeys commands will always define
        # monk_args regardless of need to re-enforce the paradigm (this is inspired by dependency injection)
        # (ex: generate_monkeys.py@main)
        elif args_count == 0:
            return function()

        # This is commented out to maintain confidence it isn't unintentionally used.
        # If at some point monk needs to pass a list of args to a function, uncomment this.
        # elif args_count > 1:
        #     return function(*args)

        elif args_count > 1:
            print_t('Running entities with monk supports only a list of monk_args or no args. View '
                    'run_as_module.py for more details (including some code you could uncomment to enable '
                    'what you are attempting.', 'error')
            return None

    else:
        if '__main__' in module.__dict__:
            return module.__dict__['__main__']()
        else:
            print_t('No main function found in module.', 'error')
