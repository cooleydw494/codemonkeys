# CodeMonkeys 🐒

A framework for automating GPT-powered tasks, from simple to complex. Sphinx docs [here](https://cooleydw494.github.io/codemonkeys).

## Overview 🌐

CodeMonkeys gives devs control over their automated GPT logic. The current focus is working on codebases but it is lovingly designed to enable automations of all kinds. This framework aims to use AI effectively, while being reliable, predictable, and tailored to your needs. There is a strong focus on only involving AI at crucial areas of strength, and using good old-fashioned code for everything else.

## Alpha Status (10-10-2023) 🚧
CodeMonkeys will soon have a stable Alpha release focused on establishing the framework's architecture/concepts to a point of relative stability, and providing a flexible, immediately useful default Automation that is instructional in how it utilizes the framework.

## Index
- [Getting Started](#getting-started-)
- [Project Structure](#project-structure-)
- [Monk CLI](#monk-cli-)
- [Monkeys](#monkeys-)
- [Env](#env-)
- [The Default Automation](#the-default-automation-)
- [Medium-term Goals](#medium-term-goals-)
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

* `/commands`: Command instances, runnable via `monk <command>`. Also handles bash/bat scripts.
* `/automations`: Automation instances, runnable via `monk -a <automation>`.
* `/barrels`: Custom or extended Barrel classes used to orchestrate multiple Automation/Monkeys.
* `/monkeys`: Custom or extended Monkey classes used to precisely configure Automation behavior.
* `/builders`: Custom or extended Builder classes for re-usable automation logic.
* `/funcs`: Custom or extended Func classes for GPT function-calling.
* `codemonkeys.defs`: A core module that dynamically exposes important PATHs for your project (ex: COMMANDS_PATH).

## Monk CLI 🐵

CodeMonkeys' CLI interface is used via the `monk` command which handles running Automations, Barrels, Commands, and built-in framework Commands. The `monk` command can be run anywhere in a CodeMonkeys project, and will always run in the context of the project root.

## Monkeys 🐒
Monkeys are your tool for specifying the exact behavior of your Automations. Your prompts, models, temperature, paths, and behavior specifications live here. The class-based approach unlocks advantages like inheritance, custom logic, and lifecycle hooks, but at heart the Monkey class maintains the simplicity of a config file. It is possible to configure your Automation behavior by doing no more than changing hard-coded class properties, not unlike editing a yaml file (but better).

You can specify a Monkey when running an Automation using the `--monkey=<name>` CLI arg.

```
from monkeys.monkey import Monkey
from monkeys.docblock_monkey import DocblockMonkey

# Load a specific Monkey directly
m = DocblockMonkey()

# Load any Monkey dynamically using your base Monkey class
m = Monkey.load(<name>)

# access properties easily
main_prompt = m.MAIN_PROMPT
```

## Env 📝
The Env class is an interface for accessing properties defined in your `.env`. On every run of the `monk` CLI, type-hinted properties that help avoid mistakes and make your IDE smarter are regenerated. You may customize or ignore your `config/env.py`, but it is used by core framework code, so _don't remove it or edit the generation tags_.

```
from config.env import Env
env = Env.get()

# access properties easily
openai_api_key = env.OPENAI_API_KEY
```

## The Default Automation 🤖

The default automation, `automations/default.py`, is a generic but complete template for running automations on files in your `WORK_PATH`. Out-of-the-box, it allows you to run GPT-powered mass file operations simply by configuring Monkeys. The default Automation is also an instructive example of using the framework, as it includes configurable implementations of all stock Monkey properties.

## Medium-term Goals 📅
Some concerns have been set aside as I prepare for a stable Alpha release. The next major areas of focus:
- Test Coverage
- More testing on Windows/Linux (Should Work ™️, but tested thoroughly on macOS only)
- Handling longer files (a major limitation currently)
- Streamlined support for fine-tuning (existing fine-tuned models already work)
- Expansion of pre-packaged Automations, Monkey config options, and Builders
  - Particular focus on function calling support and pre-packaged Funcs
- Improved error handling throughout framework (already decent, but sometimes errors are unclear)
- More intentional git strategy, and contribution docs/standards
- Improve CLI UI in general, and accessibility-focused presets for Theme config

## Attribution 🙏
All forms of attribution will be greatly appreciated, especially linking directly to this repo.
