# CodeMonkeys 🐒

A framework for automating GPT-powered tasks, from simple to complex. Read the docs [here](https://cooleydw494.github.io/codemonkeys).

## Overview 🌐

CodeMonkeys gives developers of varying levels control over their automated GPT logic, focusing on the goal of working on codebases but designed to enable automations of all kinds. Its purpose is to help you build GPT-powered automations that are reliable, predictable, and tailored to your needs. There is a strong focus on only involving AI at crucial areas of strength, and leveraging more controllable and intentional methods for everything else. There is much more to it than just automation logic, and I invite you to read on to see it for yourself.

CodeMonkeys includes a default automation to handle a wide array of automated file operations.

### Alpha Status (updated Oct 10, 2023) 🚧
CodeMonkeys will soon have a stable Alpha release. This release will focus on establishing the framework, solidifying architecture/concepts to a point of relative stability, and providing a flexible, immediately useful default Automation that is instructional in how it utilizes the framework.

There are concerns to be handled for eventual Beta release that have been set aside while focusing on a stable Alpha:
- Test Coverage
- More testing on Windows/Linux (Should Work ™️, but tested thoroughly on macOS only)
- Handling longer files (a major limitation currently)
- Streamlined support for fine-tuning (existing fine-tuned models already work)
- Expansion of pre-packaged Automations, Monkey config options, and Builders
  - Particular focus on function calling support and pre-packaged Funcs
- More intentional git strategy, and contribution docs/standards
- Improve CLI UI in general, and accessibility-focused presets for Theme config

## Index
- [Getting Started](#getting-started-)
- [Project Structure](#project-structure-)
- [Monk CLI](#monk-cli-)
- [Configuration](#configuration-)
- [Monkeys](#monkeys-)
- [Env](#env-)
- [The Default Automation](#the-default-automation-)
- [Attribution](#attribution-)


## Getting Started 🚀

First, install the framework with pip:
```
pip install codemonkeys
```

Then, use the `monk-new` command to create a new project:
```
monk-new [project_name]
```
This will scaffold a new project with the given name. _Note: CodeMonkeys treats your project as a package, so your project name should respect package name requirements (snake_case)._

`cd` into your project and run `monk` or `monk help`. If scaffolded successfully this will print a general help screen.

## Project Structure 📁
CodeMonkeys' project structure aims to allow you to build/configure/run your automations in a simple, powerful way. You're encouraged to get creative with your Automation/Command/Barrel `run()` methods, custom config properties, and utilize any additional modules/classes/dirs you create. However, the base project scaffolding is assumed by the Monk CLI and built-in config management. Don't fight these paradigms unless you're prepared to replace them.

* `monk`: CLI command exposed by core package, run from within a CodeMonkeys project.
* `commands`: Command instances, runnable via `monk <command>`. Also handles bash/bat scripts.
* `monkeys/monkey-manifest.yaml`: The centralized config file for all monkeys.
* `stor/temp/monkeys`: Individual validated/cached Monkey configs. Includes `.history` for previous versions.
* `automations`: Automation instances, runnable via `monk -a <automation>`.
* `automations/default.py`: An out-of-the-box Automation, capable of highly configurable mass file operations.
* `barrels`: Barrel instances, runnable via `monk -b <barrel>`. Barrels allow orchestration of multiple automations.
* `barrels/default.py`: Pre-packaged barrel, which enables running a series of parallel or sequential automations.
* `composables`: Custom composable classes for automation functionality, or extended core framework composables.
* `defs.py`: A core framework file exposing crucial PATHs dynamically set based on a specific project (ex: COMMANDS_PATH).

## Monk CLI 🐵

CodeMonkeys' CLI interface is used via the `monk` command which handles running Automations, Barrels, Commands, and built-in framework Commands. The `monk` command can be run anywhere in a CodeMonkeys project, and will always run in the context of the project root.

## Configuration 🛠️
CodeMonkeys has built-in configuration management, including an Env class and a Monkey class which are automatically rewritten to include any custom `.env` or `config/monkey-config-defaults` values you add. These are rewritten on every run of `monk` and allow IDE intelligence for you env/config properties.
_Note: You should never modify the Monkey or Env class within `config/framework`. These exist to allow automatic rewrites that include full support for user-defined properties._

## Monkeys 🐒
Monkeys are your tool for specifying the exact behavior of your Automations. Your prompts, models, temperature, paths, and behavior specifications live here. The class-based approach unlocks advantages like inheritance, custom logic, and lifecycle hooks, but at heart the Monkey class maintains the simplicity of a config file. It is possible to configure your Automation behavior by doing no more than changing hard-coded class properties, not unlike editing a yaml file (but better).

You can specify a Monkey when running an Automation using the `--monkey=<name>` CLI arg.

```
from config.monkeys.monkey import Monkey
from config.monkeys.docblock_monkey import DocblockMonkey

# You can also load a specific Monkey
m = DocblockMonkey()

# or simply use your base Monkey class to load any Monkey dynamically
m = Monkey.load(<name>)

# access properties easily
main_prompt = m.MAIN_PROMPT
```

## Env 📝
The Env class is a simple interface for accessing env properties, as defined in your `.env` file. You may customize your `config/env.py`, but don't edit the tags in place for property generation. On every run of the `monk` CLI, it is re-generated, injecting dynamically type-hinted properties that help you avoid mistakes and make your IDE smarter. You're free to ignore it and use whatever method you prefer, but core framework code uses your `config/env.py`, so _don't remove it_.

```
from config.env import Env
env = Env.get()

# access properties easily
openai_api_key = env.OPENAI_API_KEY
```

## The Default Automation 🤖

The default automation, `automations/default.py`, is a generic but complete template for running automations on files in your `WORK_PATH`. Out-of-the-box, it allows you to run GPT-powered mass file operations simply by configuring Monkeys. The default Automation is also an instructive example of using the framework, as it includes configurable implementations of all stock Monkey properties.

## Attribution 🙏
All forms of attribution will be greatly appreciated, especially linking directly to this repo.
