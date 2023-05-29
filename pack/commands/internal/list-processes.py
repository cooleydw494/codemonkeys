import os
import subprocess

from pack.modules.custom.theme.theme_functions import print_table, print_t, apply_theme


def main():
    # Get monk processes
    monk_processes = subprocess.run(['pgrep', '-a', 'monk'], stdout=subprocess.PIPE).stdout.decode().split('\n')[:-1]
    process_row_data = [process.split(maxsplit=1) for process in monk_processes]

    # Check if there are any ongoing monk processes
    if not process_row_data:
        print_t("No ongoing monk processes.", "important")
        return

    # Include kill commands
    for process in process_row_data:
        process.append(f"kill {process[0]}" if os.name != 'nt' else f"taskkill /PID {process[0]} /F")

    # Format monk processes for the table
    table = {
        "show_headers": True,
        "header_color": "magenta",
        "row_colors": ["cyan", "yellow", "dark_grey"],
        "headers": ["PID", "Command", "Kill Command"],
        "rows": process_row_data
    }

    print_table(table, apply_theme("Monk Processes", 'monkey'))


if __name__ == "__main__":
    main()
