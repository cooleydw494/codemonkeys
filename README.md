# CodeMonkeys 🐒

A framework for automating GPT-powered tasks, from simple to complex. Read the Sphinx documentation [here](https://cooleydw494.github.io/codemonkeys/).

## Overview 🌐

CodeMonkeys gives developers of varying skill levels control over their automated GPT logic, providing a more intentional alternative to tools like AutoGPT. The primary goal is to help you build GPT-powered automations that are reliable, predictable, and tailored to your needs, only involving AI at crucial areas of strength. The framework combines built-in utilities, composable classes for running GPT-powered tasks, and a robust configuration management system. CodeMonkeys includes a default automation to handle a wide array of mass file operations via simple configuration, but is meant to be extensible enough to enable *your* use-case.

### Alpha Status 🚧
A lot of care has been put into a solid starting point for the vision, but a lot of work remains, including: testing, expanded modular functionality such as web browsing, content chunking, memory management, alternative LLMs (including local), and much more. CodeMonkeys has an early focus on mass file operations, but is designed for growth and expansion, and to become a powerful tool for creating incredible things.

## Getting Started 🚀

First, install the framework with pip:
```
pip3 install codemonkeys
```

Then, use the `monk-new` command to create a new project:
```
monk-new [project_name]
```
This will scaffold a new project with the given name. _Note: CodeMonkeys treats your project as a package, so your project name should respect package name requirements (snake_case)._

## Project Structure Overview 📁
CodeMonkeys' project structure aims to allow you to build/configure/run your automations in a simple, powerful way. You're encouraged to get creative with your Automation/Command/Barrel `run()` methods, custom config properties, and utilize any additional modules/classes/dirs you create. However, the base project scaffolding is assumed by the Monk CLI and built-in config management. Don't fight these paradigms unless you're prepared to replace them.

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

## Monk CLI 

CodeMonkeys' CLI interface is used via the `monk` command which handles running Automations, Barrels, Commands, and built-in framework Commands. The `monk` command can be run anywhere in a CodeMonkeys project, and will always run in the context of the project root.

## Configuration Management 📝
CodeMonkeys has built-in configuration management, including an Env class and a MonkeyConfig class which are automatically rewritten to include any custom `.env` or `config/monkey-config-defaults` values you add. These are rewritten on every run of `monk` and allow IDE intelligence for you env/config properties.
_Note: You should never modify the MonkeyConfig or Env class within `config/framework`. These exist to allow automatic rewrites that include full support for user-defined properties._

### MonkeyConfig 
The MonkeyConfig class is a wrapper for a single monkey config, as defined in `monkeys/monkey-manifest.yaml`. It provides a simple interface for accessing monkey config properties via dot notation, and includes built-in validation logic.

```
from codemonkeys.utils.monkey_config.load_monkey_config import load_monkey_config

# load a config
mc = load_monkey_config('comment-monkey')

# prompt user to choose a config to load
mc = load_monkey_config()

# access a property via dot notation
main_prompt = mc.MAIN_PROMPT
```

### Env
The Env class provides a simple interface for accessing env properties, as defined in your `.env`, via dot notation. It includes built-in validation logic and supports user-defined properties.

```
from config.framework.env import Env
env = Env.get()

# access a property via dot notation
openai_api_key = env.OPENAI_API_KEY
```

## The Default Automation

The default automation, `automations/default.py`, is a generic but complete template for running automations on files in your `WORK_PATH`. It works well out of the box, and allows you to run GPT-powered mass file operations by simply using monkey configs (`monkey-manifest.yaml`). The default Automation is also a great example of the various capabilities custom automations can have. It includes optional examples of all standard monkey config properties, and serves as a good example of how to use the framework-packaged composables. Whether your custom automations require far less, far more, or more specific functionality, you can copy/paste a pretty good starting point from `automations/default.py`.

## Attribution
All forms of attribution will be appreciated, especially when linking directly to the repo.

# Things To Include
monkey-config-defaults
replace_prompt_str
cop_paths