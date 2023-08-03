import os

import psutil

from codemonkeys.entities.command import Command
from codemonkeys.utils.monk.theme_functions import print_table, print_t, apply_t


class ListProcesses(Command):
    """
    The ListProcesses class is a subclass of Command. 
    It is used to display all the running processes 
    that contain 'monk' in their name or command 
    line options.
    """

    def run(self) -> None:
        """
        Prints out a table of ongoing 'monk' processes displaying their 
        ID, command, and equivalent command to kill the process.
        """
        monk_processes = []
        for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
            try:
                cmdline = ' '.join(proc.info['cmdline']) if proc.info['cmdline'] else ''
                if 'monk' in proc.info['name'] or ' monk ' in cmdline:
                    monk_processes.append([str(proc.info['pid']), cmdline])
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass

        process_row_data = [process for process in monk_processes]

        if not process_row_data:
            print_t("No ongoing monk processes.", "important")
            return

        for process in process_row_data:
            process.append(f"taskkill /PID {process[0]} /F" if os.name == 'nt' else f"kill {process[0]}")

        table = {
            "show_headers": True,
            "header_color": "magenta",
            "row_colors": ["cyan", "yellow", "dark_grey"],
            "headers": ["PID", "Command", "Kill Command"],
            "rows": process_row_data
        }

        print_table(table, apply_t("Monk Processes", 'monkey'))
