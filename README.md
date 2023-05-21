# CodeMonkeys 🐵👨‍💻

Are you a highly-technical individual with an interest in taking more control over your automated AI coding?

. . . . a lightly-technical individual who wants to automate AI and can probably figure out how to edit a config?

. . . . a creature with the capacity to learn how to press buttons and a strong motivation to do the AI?

Welcome to CodeMonkeys, a user-friendly _and_ power-user-friendly project designed to maximize the potential of the GPT
API and streamline autonomous tasks with an emphasis on code generation and improvement. It's all about granting you,
the user, full control and freedom to shape the AI's capabilities to your specific needs and ideas. Interested? Please
scan the rest of the README, and if you find yourself intoxicated by the thought of wielding your own army of Monkeys,
read the whole thing. If a great, but typical Github README is a tightly syncopated bop that everyone can groove to
instantly, the CodeMonkeys README is a thorough and engaging concept album that conveys a subject intimately. Trust me,
the version of you that reads the whole thing will run circles around the version of you that doesn't. Take the win. Or
don't ([cheatcodes](#getting-started-)).

## About The Author

I'm David. I'm a very-full-stack engineer with more than 5 and less than 50 years of experience in software dev, mostly
web. A generic description of my roles would look something like "coder, lead coder, founder, coder". Oh, I also do not
know Python very well. This project is good in creative ways in spite of that and because of it. It may be non-ideal in
ways I don't notice, but I believe that my Baby's First Python mentality, coupled with other coding experience and
powerful AI models that can write Python very well, has led to an interesting and more-than-viable design.

## Overview 🌐

CodeMonkeys, while maintaining a strong emphasis on coding tasks, is designed to be a purposefully more focused
alternative to broad spectrum tools like AutoGPT. The goal is to reduce GPT API call wastage and provide more control,
harnessing the power of automation for tasks that are reliable, predictable, and precisely tailored to user needs, only
involving AI at crucial areas of strength. The project is built around a suite of adaptable Python scripts and
user-friendly configuration utilities. This approach ensures that while you have a solid foundation for customization,
you also maintain the efficiency and potency of the core framework. CodeMonkeys aims to strike a balance between
adaptability and specificity, providing a less feature-rich but more extensible and capable tool for your unique
automation needs.

# The Default Program (main.py)

The heart of CodeMonkeys is `main.py`, a generic but complete template for improving whatever is in your `WORK_PATH`.
This file is the default entry-point and is designed to work well out of the box, and to be powerfully customizable
using only `monkey-manifest.yaml` configurations. `main.py` is a top-down look at the default Monkey Program. During
installation, a copy of this file is stored in `programs/my-first-program`. The `programs` directory is a location for
your own variations of the main.py file, should you feel the urge to start writing your own programs. If you're thinking
_"already there, pal"_, I see you, but I'd recommend you start by playing with the monkey-manifest and default program.
If you're thinking _"that's too much, man"_, no worries, the default program and monkey-manifest are very powerful, and
the proprietary programs in the `programs` directory will be expanded.

If the default program `main.py` is the heart of CodeMonkeys, then

In addition to the monkey-manifest and main.py default program, CodeMonkeys commits to being moddable with a simple and
powerful design for using/implementing `scripts`. The `scripts` directory is...

## Getting Started 🚀

To get started, you'll want to [fork](https://help.github.com/en/articles/fork-a-repo) the CodeMonkeys repository. Once
you've done that, navigate to the CodeMonkeys directory in your terminal and run the setup script:

```

```

## Usage 🎮

CodeMonkeys operates via the `monk` command which runs Python scripts located in the `scripts` directory. For example,
to kick off a monkey, simply use `monk kickoff [monkey-name] -n50`, where `n` is the maximum number of iterations to
run. There is no default value for `-n` as a measure to encourage thoughtful use and provide a safety measure for those
less familiar with the documentation.

If a monkey name is not provided, CodeMonkeys will check the .env file for a DEFAULT_MONKEY variable. If it exists, it
will load the corresponding monkey configuration from the ../monkeys/[DEFAULT_MONKEY] directory.

## Customization and Updates 🛠

CodeMonkeys is designed to grow and adapt with you. The framework provides several built-in features that allow you to
tailor the project to your needs.

- **Monkey-Manifest**: Define and manage your custom 'monkeys' or tasks in a centralized configuration file.

- **Local `.env` Files**: Manage your environment variables locally without affecting the global settings.

- **Import/Export**: Easily share your customizations or move between different systems.

    - **Export**: Use `monk export` to create an archive that includes your custom `main.py`, monkey configurations, and
      existing backups of your main file. The export is timestamped and can be moved to other systems or shared with
      others.

    - **Import**: Use `monk import [path-to-exported-file]` to import a previously exported archive. This will replace
      your current `main.py` and monkey configurations with those in the archive. But don't worry - before anything is
      replaced, your current `main.py` is backed up with a timestamp, and your backups are merged with those from the
      import.

I strive to make CodeMonkeys easy to update, even with your customizations. However, extensive modifications may
complicate the update process. Please note that while I'm working hard to make updates as seamless as possible, it's
always a good idea to back up your work before updating.

For easy export of your `monkey-manifest.yaml`, `programs`, and all `customizable` directories, simply run

```
monk export
```

The export process will also create a `.env-backup` file that contains your current .env file. `.env-backup` is in the default .gitignore, and is not included in the export. Please also verify that you are not committing your exports if you have sensitive information outside of your .env file, such as in the `monkey-manifest.yaml` (*however, you should not do that*).

## Directory Overview 📁

* `main.py`: Your primary customization file. Created by ./install
* `monk`: The command to run scripts.
* `monkeys`: Contains configurations for different 'monkeys' or tasks.
* `scripts`: Contains Python scripts to be run via the `monk` command.
* `monkeys/monkey-manifest.yaml`: The centralized configuration file for all monkeys.

## Convenience Tools

There are some tools I've found useful in development that I've left here for the sake of simplicity for myself and to
allow others to use them.

### Commit Script

Starting whenever this was added, I'm trying hard to actually make frequent commits to document my progress, so as a
lazy person I made a commit script that allows me to type a few characters, a commit message, and then perform a git
add, a commit, and an optional push all at once. For me, this is nice, and I might start using it elsewhere. If you use
ubuntu or macOS, you can use it like this:

```bash
./c "commit message"
```

## Attribution

When forking or creating derivative works from CodeMonkeys, I kindly ask you to:

1. Clearly acknowledge the CodeMonkeys project and provide a hyperlink to the CodeMonkeys repository in the first section of your README.md file.

2. Prominently display an acknowledgement of the usage of CodeMonkeys in any application, framework, or derivative work which is built on top of the CodeMonkeys framework and is distributed through an application store, website, social media, or any other distribution method.
