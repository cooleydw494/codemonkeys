import os
import shutil
import subprocess
import sys
import time

from definitions import PYTHON_COMMAND
from pack.modules.custom.theme.theme_functions import print_t

# Check if the export filepath argument is provided
if len(sys.argv) < 2:
    print_t("Please provide the export filepath as a command-line argument.", 'error')
    sys.exit(1)

# Get the export filepath from the command-line argument
export_filepath = sys.argv[1]

# Perform a backup of the current main.py
timestamp = time.strftime("%Y%m%d%H%M%S")
backup_filename = f"pre-export-{timestamp}"
subprocess.run([PYTHON_COMMAND, "scripts/backup-main.py", backup_filename])

# Merge the backups/main directories
shutil.copytree("backups/main", "backups/main-merged", dirs_exist_ok=True)

# Determine the archive format for macOS
system = sys.platform
if system == "darwin":
    archive_format = "gztar"
elif system == "linux":
    archive_format = "tar"
else:
    archive_format = "zip"

# Extract the exported project files
shutil.unpack_archive(export_filepath, "", format=archive_format)
export_filename = os.path.basename(export_filepath).split(".")[0]

# Merge the backups/main directories from the export
shutil.copytree(f"{export_filename}/backups/main", "backups/main-merged", dirs_exist_ok=True)

# Replace the current project files with the exported files
shutil.move(f"{export_filename}/main.py", "main.py")
shutil.move(f"{export_filename}/monkeys/monkey-manifest.yaml", "monkeys/monkey-manifest.yaml")
shutil.move("backups/main-merged", "backups/main")

print_t(f"Project files imported from: {export_filepath}", 'config')
print_t(f"Backup created: {backup_filename}", 'config')
print_t("Project files successfully imported.", 'done')
