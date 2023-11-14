import sys
import traceback

from codemonkeys.utils.monk.theme_functions import input_t, print_t, verbose_logs_enabled


def handle_exception(exception: BaseException, always_exit=False, always_continue=False) -> None:
    """
    Handle common and unexpected exceptions, allowing for user-interaction on continuation.

    This function is designed to provide a consistent approach to exception handling across the
    framework. It takes care of printing the exception information, optionally including a traceback,
    and determines whether to exit the program or to prompt the user with a choice to continue or exit.

    :param exception: The exception being handled.
    :type exception: BaseException
    :param always_exit: If True, the program will exit without prompting the user.
    :type always_exit: bool
    :param always_continue: If True, the program will continue without prompting the user.
    :type always_continue: bool
    :return: None
    :rtype: None

    :raises SystemExit: On triggering an exit due to KeyboardInterrupt or user choice.

    Example:
        >>> handle_exception(ValueError("Some error"))
        (ValueError) Some error
        Do you want to continue? (y/n) y

    .. note:: KeyboardInterrupt and SystemExist cases ignore any other exit logic,
        always inferring intentional exit.
    .. warning:: Verbose logging is disabled by default. Enable verbose logs in config/theme.py to see tracebacks.
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
