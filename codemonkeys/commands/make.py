import os
import shutil

from codemonkeys.cm_paths import CM_EXAMPLE_COMMAND_PATH, CM_EXAMPLE_AUTOMATION_PATH, CM_EXAMPLE_BARREL_PATH
from codemonkeys.defs import COMMANDS_PATH, AUTOMATIONS_PATH, BARRELS_PATH, MONKEYS_PATH, USER_BASE_MONKEY_PATH
from codemonkeys.entities.command import Command
from codemonkeys.types import OStr


class Make(Command):
    """
    The Make Class is a command that copies an example entity in a specified path and renames it accordingly.
    
    :param str entity_type: The type of the entity to be created, e.g., command, automation, barrel.
    :param str entity_name: The name of the entity to be created.
    """
    required_arg_keys: list = ['entity_type', 'entity_name']
    unnamed_arg_keys: list = ['entity_type', 'entity_name']

    entity_type: OStr = None
    entity_name: OStr = None

    ENTITY_TYPE_INFO: dict = {
        'command': (COMMANDS_PATH, CM_EXAMPLE_COMMAND_PATH, 'ExampleCommand'),
        'automation': (AUTOMATIONS_PATH, CM_EXAMPLE_AUTOMATION_PATH, 'ExampleAutomation'),
        'barrel': (BARRELS_PATH, CM_EXAMPLE_BARREL_PATH, 'ExampleBarrel'),
        'monkey': (MONKEYS_PATH, USER_BASE_MONKEY_PATH, 'Monkey')
    }

    def run(self) -> None:
        """
        The main execution method for the Make command.
        
        :raises ValueError: If the entity_name isn't in a valid format (kebab-case)
        """

        if self.entity_type == 'monkey' and self.entity_name == 'monkey':
            raise ValueError("You cannot create a Monkey named 'monkey' (that's where you set defaults, silly!).")

        if not self.entity_name.replace('-', '').replace('_', '').isalpha():
            raise ValueError(f"Invalid name: {self.entity_name}. Please specify in kebab-case (e.g. entity-name).")

        # Get info based on the entity type
        entity_path, example_path, example_name = self.ENTITY_TYPE_INFO.get(self.entity_type)

        new_entity_path = os.path.join(entity_path, f'{self.entity_name}.py')
        shutil.copy(example_path, new_entity_path)

        with open(new_entity_path, 'r') as f:
            file_contents = f.read()

        new_class_name = self.entity_name.title().replace('-', '').replace('_', '')
        file_contents = file_contents.replace(example_name, new_class_name)

        # When making a Monkey, we need to fix base class import/usage
        if self.entity_type == 'monkey':
            base_import = f'from codemonkeys.config.monkey import {new_class_name} as Base'
            file_contents = file_contents.replace(base_import, 'from config.monkeys.monkey import Monkey')
            class_definition = f'{new_class_name}(Base):'
            file_contents = file_contents.replace(class_definition, f'{new_class_name}(Monkey):')

        with open(new_entity_path, 'w') as f:
            f.write(file_contents)
