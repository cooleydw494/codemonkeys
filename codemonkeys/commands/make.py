import os
import shutil

from codemonkeys.entities.command import Command
from codemonkeys.cmdefs import CM_EXAMPLE_COMMAND_PATH, CM_EXAMPLE_AUTOMATION_PATH, CM_EXAMPLE_BARREL_PATH
from codemonkeys.defs import COMMANDS_PATH, AUTOMATIONS_PATH, BARRELS_PATH


class Make(Command):
    """
    The Make Class is a command that copies an example entity in a specified path and renames it accordingly.
    
    :param str entity_type: The type of the entity to be created, e.g., command, automation, barrel.
    :param str entity_name: The name of the entity to be created.
    """
    required_arg_keys = ['entity_type', 'entity_name']
    unnamed_arg_keys = ['entity_type', 'entity_name']

    entity_type: str = None
    entity_name: str = None

    ENTITY_TYPE_INFO = {
        'command': (COMMANDS_PATH, CM_EXAMPLE_COMMAND_PATH, 'ExampleCommand'),
        'automation': (AUTOMATIONS_PATH, CM_EXAMPLE_AUTOMATION_PATH, 'ExampleAutomation'),
        'barrel': (BARRELS_PATH, CM_EXAMPLE_BARREL_PATH, 'ExampleBarrel')
    }

    def run(self) -> None:
        """
        The main execution method for the Make command.
        
        :raises ValueError: If the entity_name isn't in a valid format (kebab-case)
        """
        if not self.entity_name.replace('-', '').isalpha():
            raise ValueError(f"Invalid name: {self.entity_name}. Please specify in kebab-case (e.g. entity-name).")

        # Get info based on the entity type
        entity_path, example_path, example_name = self.ENTITY_TYPE_INFO.get(self.entity_type)

        new_entity_path = os.path.join(entity_path, f'{self.entity_name}.py')
        shutil.copy(example_path, new_entity_path)

        with open(new_entity_path, 'r') as f:
            file_contents = f.read()

        file_contents = file_contents.replace(example_name, self.entity_name.title().replace('-', ''))

        with open(new_entity_path, 'w') as f:
            f.write(file_contents)
