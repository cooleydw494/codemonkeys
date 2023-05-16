# CodeMonkeys 🐵👨‍💻

Welcome to CodeMonkeys, a dynamic and user-friendly project designed to maximize the potential of the GPT API and streamline autonomous tasks with an emphasis on code generation and improvement. It's all about granting you, the user, full control and freedom to shape the AI's capabilities to your specific needs and ideas.

## Overview 🌐

CodeMonkeys, while primarily focusing on coding, is highly adaptable and can be tailored to a variety of use cases. The project is structured around a set of flexible Python scripts and easy-to-edit configuration tools. This provides a solid starting point for your customization, while preserving the simplicity and power of the underlying framework.

The heart of CodeMonkeys is `main.py.start-here`, a generic template for improving your codebase. During installation, a copy of this file named `main.py` is created and is the primary method for customization. This file is added to .gitignore to avoid interference with your unique modifications.

## Getting Started 🚀

To get started, you'll want to [fork](https://help.github.com/en/articles/fork-a-repo) the CodeMonkeys repository. Once you've done that, navigate to the CodeMonkeys directory in your terminal and run the install script with the following commands:

```bash
chmod +x install.sh
./install.sh

## Usage 🎮

CodeMonkeys operates via the `monk` command which runs Python scripts located in the `scripts` directory. For example, to kick off a monkey, simply use `monk kickoff [monkey-name] -n50`, where `n` is the maximum number of iterations to run. There is no default value for `-n` as a measure to encourage thoughtful use and provide a safety measure for those less familiar with the documentation.

You can create a backup of your current `main.py` file at any time by running `monk backup-main "optional-backup-name-defaults-to-timestamp"`. This ensures your unique modifications are safe and sound.

## Customization and Updates 🛠

This project is designed to grow with you. The built-in framework features like `monkey-manifest`, local `.env` files, and others allow you to tailor the project to your needs. To export your customizations, use `monk export`, and to import them, use `monk import [path-to-exported-gz-file]`.

We aim to make CodeMonkeys easy to update, even with your customizations. However, extensive modifications may complicate the update process. Rest assured, we are working hard to make updates as seamless as possible.

## Directory Structure 📁

Here is the directory structure of CodeMonkeys:

.
├── main.py
├── monk
├── monkeys
│   ├── bridge-monkey
│   ├── comment-monkey
│   ├── generic-monkey
│   ├── monkey-manifest.yaml
│   ├── style-monkey
│   └── task-monkey
└── scripts
    ├── convert-dir-to-txt.py
    ├── generate-monkeys.py
    ├── list-code-monkey-files.py
    ├── monkey-reset
    └── select-next-file.py


* `main.py`: Your primary customization file.
* `monk`: The command to run scripts.
* `monkeys`: Contains configurations for different 'monkeys' or tasks.
* `scripts`: Contains Python scripts to be run via the `monk` command.
* `monkey-manifest.yaml`: The centralized configuration file for all monkeys.

