import os
import subprocess

from personality.custom.visuals import print_table, print_nice


def main():
    print_nice("Displaying ongoing monk processes\n", color="yellow")

    # Get monk processes
    monk_processes = subprocess.run(['pgrep', '-a', 'monk'], stdout=subprocess.PIPE).stdout.decode().split('\n')[:-1]
    process_row_data = [process.split(maxsplit=1) for process in monk_processes]
    # Include kill commands
    for process in process_row_data:
        process.append(f"kill {process[0]}" if os.name != 'nt' else f"taskkill /PID {process[0]} /F")

    # Format monk processes for the table
    table = {
        "show_headers": True,
        "header_color": "magenta",
        "row_colors": ["cyan", "yellow", "green"],
        "headers": ["PID", "Command", "Kill Command"],
        "rows": process_row_data
    }

    print_table(table, "🐵 Monk Processes")


if __name__ == "__main__":
    main()
