import os
import sys
import shutil
import time
import subprocess

# Check if the export filepath argument is provided
if len(sys.argv) < 2:
    print("⚠️ Please provide the export filepath as a command-line argument.")
    exit(1)

# Get the export filepath from the command-line argument
export_filepath = sys.argv[1]

# Perform a backup of the current main.py
timestamp = time.strftime("%Y%m%d%H%M%S")
backup_filename = f"pre-export-{timestamp}"
subprocess.run(["python", "scripts/backup-main.py", backup_filename])

# Merge the main-backups directories
shutil.copytree("main-backups", "main-backups-merged", dirs_exist_ok=True)

# Determine the archive format for macOS
system = sys.platform
if system == "darwin":
    archive_format = "gztar"
elif system == "linux":
    archive_format = "tar"
else:
    archive_format = "zip"

# Extract the exported project files
shutil.unpack_archive(export_filepath, ".", format=archive_format)
export_filename = os.path.basename(export_filepath).split(".")[0]

# Merge the main-backups directories from the export
shutil.copytree(f"{export_filename}/main-backups", "main-backups-merged", dirs_exist_ok=True)

# Replace the current project files with the exported files
shutil.move(f"{export_filename}/main.py", "main.py")
shutil.move(f"{export_filename}/monkeys/monkey-manifest.yaml", "monkeys/monkey-manifest.yaml")
shutil.move("main-backups-merged", "main-backups")

print(f"✅ Project files imported from: {export_filepath}")
print(f"✅ Backup created: {backup_filename}")
print("✅ Project files successfully updated.")

