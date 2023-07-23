# CodeMonkeys 🐵

A framework for automating GPT-powered tasks, from simple to complex. CodeMonkeys enables your nitty gritty use-case, and includes a default automation to handle a wide array of mass file operations using a simple yaml config.

## Overview 🌐

CodeMonkeys is designed to give developers of varying skill levels more control over their automated GPT logic and provide a more intentional alternative to tools like AutoGPT. The primary goal is to help you build GPT-powered automations that are reliable, predictable, and tailored to your needs, only involving AI at crucial areas of strength. The framework combines built-in utilities, composable classes for running GPT-powered tasks, and a robust configuration management system. CodeMonkeys provides a simple developer experience that can become as complex as you need it to be.

## Getting Started 🚀

### Installation

First, install the framework with pip:
```
pip3 install codemonkeys
```

Then, use the `monk-new` command to create a new project:
```
monk-new [project_name]
```
This will create a new directory with your project's name, and scaffold all the dirs and files you need to get started.
_Note: Because CodeMonkeys treats your project as a package to enable a smooth experience, your project name should follow package name requirements (just stick to lowercase letters and underscores)._

## Project Structure Overview 📁
A CodeMonkeys project is meant to be open-ended, but the base structure is designed to hold your hand and allow you to build/configure/run your automations in a simple, powerful way. Get creative with what you do in your Automation/Command/Barrel `run()` methods, add custom props to the `.env` or MonkeyConfig, add a directory of helper functions, do whatever you want. Just remember that the Monk CLI and configuration management system is there to help you. Don't fight it unless you're prepared to replace it.

* `monk`: CLI command exposed by core package, run from within a CodeMonkeys project.
* `commands`: Command instances, runnable via `monk <command>`. Also handles bash/bat scripts.
* `monkeys/monkey-manifest.yaml`: The centralized config file for all monkeys.
* `stor/temp/monkeys`: Individual validated/cached monkey configs. Includes `.history` for previous versions.
* `automations`: Automation instances, runnable via `monk -a <automation>`.
* `automations/default.py`: An out-of-the-box Automation, capable of highly configurable mass file operations.
* `barrels`: Barrel instances, runnable via `monk -b <barrel>`. Barrels allow orchestration of multiple automations.
* `barrels/default.py`: Pre-packaged barrel, which enables running a series of parallel or sequential automations.
* `composables`: Custom composable classes for automation functionality, or extended core framework composables.
* `defs.py`: A core framework file exposing crucial PATHs dynamically set based on a specific project (ex: COMMANDS_PATH).

## Monk CLI 🐒

CodeMonkeys' CLI interface is used via the `monk` command which handles running Automations, Barrels, Commands, and built-in framework Commands. The `monk` command can be run anywhere in a CodeMonkeys project, and will always run in the context of the project root.

## Configuration Management 📝
CodeMonkeys has built-in configuration management, including an Env class and a MonkeyConfig class which are automatically rewritten to include any custom `.env` or `config/monkey-config-defaults` values you add. These are rewritten on every run of `monk` and allow IDE intelligence for you env/config properties.
_Note: You should never modify the MonkeyConfig or Env class within `config/framework`. These exist to allow automatic rewrites that include full support for user-defined properties._

### MonkeyConfig 
The MonkeyConfig class is a wrapper for individual monkey configs, as defined in `monkeys/monkey-manifest.yaml`. It provides a simple interface for accessing monkey config properties via dot notation, and includes some built-in validation logic. There is some other advanced functionality available, as of now undocumented.

### Env
The Env class is a wrapper for the `.env` file, and provides a simple interface for accessing env properties via dot notation. Like the MonkeyConfig, it includes some built-in validation logic and will be automatically rewritten to support any user-defined properties.

## The Default Automation

The default automation, `automations/default.py`, is a generic but complete template for running automations on files in your `WORK_PATH`. It works well out of the box, and allows you to run GPT-powered mass file operations by simply using monkey configs (`monkey-manifest.yaml`). The default Automation is also a great example of the various capabilities custom automations can have. It includes optional examples of all standard monkey config properties, and serves as a good example of how to use the framework-packaged composables. Whether your custom automations require far less, far more, or more specific functionality, you can copy/paste a pretty good starting point from `automations/default.py`.

## Attribution

When forking or creating derivative works from CodeMonkeys, I kindly ask you to:

1. Clearly acknowledge the CodeMonkeys project and provide a hyperlink to the CodeMonkeys repository in the first
   section of your README.md file.
2. Prominently display an acknowledgement of the usage of CodeMonkeys in any application, framework, or derivative work
   which is built on top of the CodeMonkeys framework and is distributed through an application store, website, social
   media, or any other distribution method.
3. Although I expect no acknowledgement when CodeMonkeys is used as a tool to accomplish things, any mention of its
   usefulness is greatly appreciated.


# Things To Include
psuedo-package
core/usr
monkey-config class
env class
monkey-config-defaults
add-monkey
auto-generation of monkeyconfig and env and .env.default
replace_prompt_str
cop_paths