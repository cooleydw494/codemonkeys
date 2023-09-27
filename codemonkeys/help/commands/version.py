from codemonkeys.utils.monk.theme_functions import print_t, print_table
from codemonkeys.defs import nl

print_t(f"Version Command Help{nl}", "important")

print_t("The `version` command prints out the current version of the CodeMonkeys software. "
        "It is useful when you need to verify the version of the CodeMonkeys software you are currently using.{nl}")

print_t(f"Usage: `monk version`{nl}", "info")

# Prints a sample output for the version command.
print_t("Example Output:", "important")
print_t("CodeMonkeys v1.0", "monkey")

print_t("Version command is simple and straightforward to use- just type in `monk version`, "
        f"and it will display the current version of CodeMonkeys software.{nl}")

print()
print_t("Remember: Regularly updating your software ensures you have the latest features and patches.", "warning")
