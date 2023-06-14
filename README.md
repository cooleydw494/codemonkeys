# CodeMonkeys 🐵

Are you

... a highly-technical individual with an interest in taking more control over your automated AI coding?

... a lightly-technical individual who wants to automate AI and can probably figure out how to edit a config?

... a creature with the capacity to learn how to press buttons and a strong motivation to do the AI?


## Overview 🌐

CodeMonkeys, while maintaining a strong emphasis on coding tasks, is designed to be a purposefully more focused
alternative to broad spectrum tools like AutoGPT. The goal is to reduce GPT API call wastage and provide more control,
harnessing the power of automation for tasks that are reliable, predictable, and precisely tailored to user needs, only
involving AI at crucial areas of strength. The project is built around a suite of adaptable Python scripts and
user-friendly config utilities. This approach ensures that while you have a solid foundation for customization,
you also maintain the efficiency and potency of the core framework. CodeMonkeys aims to strike a balance between
adaptability and specificity, providing a less feature-rich but more extensible and capable tool for your unique
automation needs.

# The Default Automation

The heart of CodeMonkeys is `main.py`, a generic but complete template for improving whatever is in your `WORK_PATH`.
This file is the default entry-point and is designed to work well out of the box, and to be powerfully custom
using only `monkey-manifest.yaml` configs. `main.py` is a top-down look at the default Monkey Program. During
installation, a copy of this file is stored in `programs/my-first-program`. The `programs` directory is a location for
your own variations of the main.py file, should you feel the urge to start writing your own programs. If you're thinking
_"already there, pal"_, I see you, but I'd recommend you start by playing with the monkey-manifest and default program.
If you're thinking _"that's too much, man"_, no worries, the default program and monkey-manifest are very powerful, and
the proprietary programs in the `programs` directory will be expanded.

If the default program `main.py` is the heart of CodeMonkeys, then

In addition to the monkey-manifest and main.py default program, CodeMonkeys commits to being moddable with a simple and
powerful design for using/implementing `scripts`. The `scripts` directory is...

## Getting Started 🚀

You have three options (try #1 first):

1. [Clone](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) CodeMonkeys
   to use as an automation tool. (or contribute 🥺)
2. [Fork](https://docs.github.com/en/get-started/quickstart/fork-a-repo) CodeMonkeys to use as a framework for making
   your own automation tool.
3. [You]() do you, boo-boo. The line between tool/framework is blurry enough for the weird thing you're thinking.

This is a source package. It isn't installed per se, but is added to Python's `sys.path` in the setup script to allow
easy module imports while maintaining a paradigm that serves the framework side of things.

**Important:** Whatever your intentions, co-existing local repos must have distinct directory names. I think this
project is best as a source package overall, but I'm relying on `sys.path` for global imports so namespacing is required
or Python cannot accurately select modules. To fix imports run `monk fix-namespace`.

If you're using 💻🐒s as a framework this is a good way to rename the project. The source code also makes use of the
directory name in this spirit in other ways I won't go into right now.

Run the setup script when you're ready:

```
python3 setup.py
```

I have relative confidence this works well on macOS/Linux, and I've tried to handle Windows well without over-committing
at this early stage. If you have issues with Windows at any time, please open an issue and give me all the info you can.

## Usage 🎮

CodeMonkeys operates via the `monk` command which runs Python scripts located in the `scripts` directory. For example,
to kick off a monkey, simply use `monk kickoff [monkey-name] -n50`, where `n` is the maximum number of iterations to
run. There is no default value for `-n` as a measure to encourage thoughtful use and provide a safety measure for those
less familiar with the documentation.

## Customization and Updates 🛠

CodeMonkeys is designed to grow and adapt with you. The framework provides several built-in features that allow you to
tailor the project to your needs.

- **Monkey-Manifest**: Define and manage your custom 'monkeys' or tasks in a centralized config file.

- **Local `.env` Files**: Manage your environment variables locally without affecting the global settings.

- **Import/Export**: Easily share your customizations or move between different systems.

    - **Export**: Use `monk export` to create an archive that includes your custom `main.py`, monkey configs, and
      existing backups of your main file. The export is timestamped and can be moved to other systems or shared with
      others.

    - **Import**: Use `monk import [path-to-exported-file]` to import a previously exported archive. This will replace
      your current `main.py` and monkey configs with those in the archive. But don't worry - before anything is
      replaced, your current `main.py` is backed up with a timestamp, and your backups are merged with those from the
      import.

I strive to make CodeMonkeys easy to update, even with your customizations. However, extensive modifications may
complicate the update process. Please note that while I'm working hard to make updates as seamless as possible, it's
always a good idea to back up your work before updating.

For easy export of your `monkey-manifest.yaml`, `automations`, `barrels`, and `custom` directories, simply run

```
monk export
```

The export process will also create a `.env-backup` file that contains your current .env file. `.env-backup` is in the
default .gitignore, and is not included in the export. Please also verify that you are not committing your exports if
you have sensitive information outside your .env file, such as in the `monkey-manifest.yaml` (*please don't do that
actually*).

## Framework Overview 📁

* `monk` or `monk.py`: CodeMonkeys CLI base command.
* `pack`: A "pseudo-package" structured for easy inspection/modification.
* `commands`: Python, bash, or bat scripts to be run via the `monk` command.
* `monkeys`: Generated configs for different 'monkeys' and backups of previous configs.
* `monkeys/monkey-manifest.yaml`: The centralized config file for all monkeys.
* `automations`: Python scripts that use monkey configs to run automations.
* `automations/default.py`: Pre-packaged automation, which enables a range of tasks via monkey configs
* `barrels`: Python scripts meant to orchestrate more than one automation.
* `barrels/default.py`: Pre-packaged barrel, which enables running a series of parallel or sequential automations.
* `modules`: Python modules for both framework support and customized functionality.
* `definitions.py`: A root-level file providing absolute path variables for both framework and custom use.

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