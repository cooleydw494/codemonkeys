import os
import shutil

from codemonkeys.cm_paths import CM_EXAMPLE_COMMAND_PATH, CM_EXAMPLE_AUTOMATION_PATH, CM_EXAMPLE_BARREL_PATH, \
    CM_EXAMPLE_FUNC_PATH
from codemonkeys.defs import COMMANDS_PATH, AUTOMATIONS_PATH, BARRELS_PATH, MONKEYS_PATH, USER_BASE_MONKEY_PATH, \
    FUNCS_PATH
from codemonkeys.entities.command import Command
from codemonkeys.types import OStr


class Make(Command):
    """
    The Make command is a CLI command to generate boilerplate code for new entities such as commands, automations,
    barrels, or funcs.

    This command streamlines the creation of new entities by copying and renaming example entity files accordingly.

    :param entity_type: The type of the entity to be created. ('command', 'automation', 'barrel', 'func', or 'monkey')
    :type entity_type: str
    :param entity_name: The name of the entity to be created
                        (snake-case for commands, automations, barrels & snail_case for funcs, monkeys)
    :type entity_name: str

    :raises ValueError: If 'entity_name' is not specified in a valid format for its entity type

    Example:
        >>> monk make command my-command
        # This will create a new command named 'test-command' in the commands directory.
    """
    required_arg_keys: list = ['entity_type', 'entity_name']
    unnamed_arg_keys: list = ['entity_type', 'entity_name']

    entity_type: OStr = None
    entity_name: OStr = None

    ENTITY_TYPE_INFO: dict = {
        'command': (COMMANDS_PATH, CM_EXAMPLE_COMMAND_PATH, 'ExampleCommand'),
        'automation': (AUTOMATIONS_PATH, CM_EXAMPLE_AUTOMATION_PATH, 'ExampleAutomation'),
        'barrel': (BARRELS_PATH, CM_EXAMPLE_BARREL_PATH, 'ExampleBarrel'),
        'func': (FUNCS_PATH, CM_EXAMPLE_FUNC_PATH, 'ExampleFunc'),
        'monkey': (MONKEYS_PATH, USER_BASE_MONKEY_PATH, 'Monkey'),
    }

    def run(self) -> None:
        """
        Execute the creation of a new entity file based on the provided arguments.

        This method handles the logic for creating a new entity by copying an example file, renaming it,
        and adjusting its contents as necessary to reflect the new entity's name and type. It enforces naming
        conventions and ensures that the new entity's class name matches the expected format for its type.

        :raises ValueError: If 'entity_name' is not specified in a valid format for its entity type or if attempting
        to create a Monkey named 'monkey'.
        """

        if self.entity_type == 'monkey' and self.entity_name == 'monkey':
            raise ValueError("You cannot create a Monkey named 'monkey' (that's where you set defaults, silly!).")

        # Instead of throwing an error for invalid snake/kebab case, we'll just fix it
        if self.entity_type in ['monkey', 'func'] and '-' in self.entity_name:
            self.entity_name = self.entity_name.replace('-', '_')
        if self.entity_type not in ['monkey', 'func'] and '_' in self.entity_name:
            self.entity_name = self.entity_name.replace('_', '-')

        if not self.entity_name.replace('-', '').replace('_', '').isalpha():
            raise ValueError(f"Invalid name: {self.entity_name}. Please specify in kebab-case or snake_case.")

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
            base_import = f'from codemonkeys.entities.monkey import {new_class_name} as Base'
            file_contents = file_contents.replace(base_import, 'from monkeys.monkey import Monkey')
            class_definition = f'{new_class_name}(Base):'
            file_contents = file_contents.replace(class_definition, f'{new_class_name}(Monkey):')

        if self.entity_type == 'func':
            file_contents = file_contents.replace('func_name', self.entity_name)

        with open(new_entity_path, 'w') as f:
            f.write(file_contents)
