from codemonkeys.base_entities.command_class import Command
from codemonkeys.utils.monk.theme_functions import print_t
from codemonkeys.defs import THEME_CONFIG_PATH, nl


class ToggleLightMode(Command):

    def run(self) -> None:

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
