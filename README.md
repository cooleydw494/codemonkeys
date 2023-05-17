# CodeMonkeys 🐵👨‍💻

Welcome to CodeMonkeys, a dynamic and user-friendly project designed to maximize the potential of the GPT API and streamline autonomous tasks with an emphasis on code generation and improvement. It's all about granting you, the user, full control and freedom to shape the AI's capabilities to your specific needs and ideas.

## Overview 🌐

CodeMonkeys, while primarily focusing on coding, is highly adaptable and can be tailored to a variety of use cases. The project is structured around a set of flexible Python scripts and easy-to-edit configuration tools. This provides a solid starting point for your customization, while preserving the simplicity and power of the underlying framework.

The heart of CodeMonkeys is `main.py.start-here`, a generic template for improving your codebase. During installation, a copy of this file named `main.py` is created and is the primary method for customization. This file is added to .gitignore to avoid interference with your unique modifications.

## Getting Started 🚀

To get started, you'll want to [fork](https://help.github.com/en/articles/fork-a-repo) the CodeMonkeys repository. Once you've done that, navigate to the CodeMonkeys directory in your terminal and run the install script with the following commands:

For Mac/Ubuntu
```bash
scripts/internal/install/install.sh
```
For Windows
```bash
call scripts\internal\install\install.bat
```

## Usage 🎮

CodeMonkeys operates via the `monk` command which runs Python scripts located in the `scripts` directory. For example, to kick off a monkey, simply use `monk kickoff [monkey-name] -n50`, where `n` is the maximum number of iterations to run. There is no default value for `-n` as a measure to encourage thoughtful use and provide a safety measure for those less familiar with the documentation.

If a monkey name is not provided, CodeMonkeys will check the .env file for a DEFAULT_MONKEY variable. If it exists, it will load the corresponding monkey configuration from the ../monkeys/[DEFAULT_MONKEY] directory.

You can create a backup of your current `main.py` file at any time by running `monk backup-main "optional-backup-name-defaults-to-timestamp"`. This ensures your unique modifications are safe and sound.

## Customization and Updates 🛠

CodeMonkeys is designed to grow and adapt with you. The framework provides several built-in features that allow you to tailor the project to your needs.

- **Monkey-Manifest**: Define and manage your custom 'monkeys' or tasks in a centralized configuration file.

- **Local `.env` Files**: Manage your environment variables locally without affecting the global settings.

- **Import/Export**: Easily share your customizations or move between different systems.

    - **Export**: Use `monk export` to create an archive that includes your custom `main.py`, monkey configurations, and backups of your main file. The export is timestamped and can be moved to other systems or shared with others.

    - **Import**: Use `monk import [path-to-exported-gz-file]` to import a previously exported archive. This will replace your current `main.py` and monkey configurations with those in the archive. But don't worry - before anything is replaced, your current `main.py` is backed up with a timestamp, and your backups are merged with those from the import.

We strive to make CodeMonkeys easy to update, even with your customizations. However, extensive modifications may complicate the update process. Please note that while we're working hard to make updates as seamless as possible, it's always a good idea to back up your work before updating.

For easy backup of your current `main.py`, simply run `monk backup-main "optional-backup-name-defaults-to-timestamp"`.

## Directory Overview 📁

* `main.py`: Your primary customization file. Created by ./install
* `monk`: The command to run scripts.
* `monkeys`: Contains configurations for different 'monkeys' or tasks.
* `scripts`: Contains Python scripts to be run via the `monk` command.
* `monkeys/monkey-manifest.yaml`: The centralized configuration file for all monkeys.

## Convenience Tools
There are some tools I've found useful in development that I've left here for the sake of simplicity for myself and to allow others to use them.

# Commit Script
Starting whenever this was added, I'm trying hard to actually make frequent commits to document my progress, so as a lazy person I made a commit script that allows me to type a few characters, a commit message, and then perform a git add, a commit, and an optional push all at once. For me, this is nice, and I might start using it elsewhere. If you use ubuntu or macOS, you can use it like this:
```bash
./c "commit message"
```
