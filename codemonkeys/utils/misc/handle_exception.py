import traceback
import sys

from codemonkeys.utils.monk.theme_functions import input_t, print_t, verbose_logs_enabled


def handle_exception(exception: BaseException, always_exit=False, always_continue=False) -> None:
    """
    This function is a catch-all for common exception handling logic and unexpected exceptions.

    Print Exception information w/ traceback, handling some generally applicable cases (i.e. KeyboardInterrupt),
    and optionally prompting the user to continue or exit.

    Note: KeyboardInterrupt and SystemExist cases ignore any other exit logic, always inferring intentional exit

    :param exception: The exception to handle.
    :param always_exit: Disable user option to continue.
    :param always_continue: Disable user option to exit.
    :return: None
    """

    # Note, at this time, many exceptions are handled the same, but left in this format for future customization

    if isinstance(exception, KeyboardInterrupt):
        print_t(f"Exiting due to KeyboardInterrupt from user.", 'quiet')
        sys.exit(0)
    if isinstance(exception, SystemExit):
        return
    elif isinstance(exception, (FileNotFoundError, PermissionError)):
        print_t(f"({type(exception).__name__}) {exception}", 'error')

    elif isinstance(exception, (ValueError, TypeError, KeyError, IndexError)):
        print_t(f"({type(exception).__name__}) {exception}", 'error')

    elif isinstance(exception, (TimeoutError, ConnectionError)):
        print_t(f"({type(exception).__name__}: {exception}", 'error')

    else:
        print_t(f"(Unexpected {type(exception).__name__}: {exception}", 'error')

    # Print the traceback
    if verbose_logs_enabled():
        print_t("Traceback:")
        traceback.print_tb(exception.__traceback__)
    else:
        print_t("Enable verbose logs in config/theme.py to see tracebacks.")

    if always_exit:
        sys.exit(1)

    if not always_continue:
        user_input = input_t("Do you want to continue?", '(y/n)')
        if user_input.lower() != 'y':
            sys.exit(1)
