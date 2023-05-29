import glob
import os
import sys

from definitions import COMMANDS_PATH, AUTOMATIONS_PATH, BARRELS_PATH, MODULES_PATH
from pack.modules.custom.theme.theme_functions import print_t


def get_entity_paths():
    return {
        'command': COMMANDS_PATH,
        'automation': AUTOMATIONS_PATH,
        'barrel': BARRELS_PATH,
        'module': MODULES_PATH,
    }


def verify_unique_entity_names():
    entity_paths = get_entity_paths()

    for entity_type, path in entity_paths.items():
        entity_files = glob.glob(f"{path}/*")
        entity_files = [file for file in entity_files if file.endswith(('.py', '.bash', '.bat'))]

        file_name_to_paths = {}
        for file in entity_files:
            filename = os.path.basename(file)
            name, _ = os.path.splitext(filename)
            if name not in file_name_to_paths:
                file_name_to_paths[name] = []
            file_name_to_paths[name].append(file)

        for name, paths in file_name_to_paths.items():
            if len(paths) > 1:
                print_t(f"Error: Multiple entities with the same name '{name}' found in the '{entity_type}' path.",
                        'error')
                print_t(f"These are the problematic entities:", 'error')
                for sub_path in paths:
                    print_t(f"- {sub_path}", 'error')
                print_t("The matching logic of CodeMonkeys is designed to be simple and powerful, but requires unique "
                        "entity names within each entity path.", 'error')
                print_t("Please rename one of the user-created entities. Do not rename framework-packaged entities to "
                        "ensure proper functionality of the framework.", 'error')
                sys.exit(1)