from codemonkeys.entities.command import Command
from codemonkeys.defs import THEME_CONFIG_PATH, nl
from codemonkeys.utils.monk.theme_functions import print_t


class ToggleLightMode(Command):
    """
    ToggleLightMode is a subclass of the Command class. Its primary function is
    to allow for toggling of Light Mode in the application's user interface.
    """

    def run(self) -> None:
        """
        Handles the reading of the theme configuration file, defines whether the 
        Light Mode is currently enabled or not, and then toggles its state.
        """

        with open(THEME_CONFIG_PATH, "r+") as file:
            lines = file.readlines()
            file.seek(0)
            for line in lines:
                if "light_mode_enabled" in line:
                    is_light_mode = "True" in line
                    print_t(f"{'Disabling' if is_light_mode else 'Enabling'} Light Mode...", 'monkey')
                    if is_light_mode:
                        line = f"light_mode_enabled: bool = False{nl}"
                    else:
                        line = f"light_mode_enabled: bool = True{nl}"
                file.write(line)
            file.truncate()
