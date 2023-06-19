
from source.utils.monk.theme.theme_functions import print_t


def main():
    print_t("Parse Monk Args Help", "important")
    print_t("parse_monk_args.py is a module responsible for parsing command-line arguments "
            "passed to the Monk CLI within the CodeMonkeys framework.", "info")

    print_t("Functionality", "special")
    print_t("parse_monk_args.py provides a utility function 'parse_monk_args' that returns:"
            "\n- Parsed arguments from command-line"
            "\n- Any unknown arguments detected"
            "\n- The chosen action to perform (default is 'run')"
            "\n- The specified entity to interact with"
            "\n- The type of entity (command, module, automation, or barrel)", "info")

    print_t("Example Usage", "special")
    print_t("To use parse_monk_args in your script, simply import the function, and call it:"
            "\n\nfrom parse_monk_args import parse_monk_args"
            "\nargs, unknown_args, action, entity, entity_type = parse_monk_args()", "file")

    print_t("Important Notes", "special")
    print_t("- It defines command-line flags to specify desired actions and entity types."
            "\n- Actions include: run, edit, print, copy-path, copy-contents, and help."
            "\n- Entity types include: module, automation, and barrel."
            "\n- parse_monk_args will apply appropriate defaults based on given inputs, "
            "for example, if 'module' type is provided but no action is specified, the default "
            "action for modules is 'edit'.", "info")

    print_t("By incorporating parse_monk_args.py into your CodeMonkeys project, you're able "
            "to manage and execute command-line operations efficiently and handle desired "
            "actions with ease.", "tip")

if __name__ == "__main__":
    main()
