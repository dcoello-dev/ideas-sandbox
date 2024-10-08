# SANDBOX

After a few years trying different notes applications (notion, obsidian ...) I couldnt integrate any of then in my development workflow, in the end I ended going to my personal Github repos looking for an example of what I wanted and then copy paste it.

Not only look for my notes was a problem, to create new code notes was a mess, I use to write my code notes or snippets in Godbolt and then copy the code snippet into markdown or just add the Godbolt link into the note.

With this two use cases in mind:
- Look for owned examples on how to do a specific thing.
- Have an environment that allows me to create new ideas and things as small examples.

I decided to create my own tool that can fit my requirements:
- Flexible to be use with any programming language.
- Easy to integrate with any code editor so I can have godbolt like local experience.
- Easy to look for my ideas (code notes) so I can have my own list of examples always available.
- I am the proprietary of my ideas so I can store where I want whether it is a git repo or local folder.

With this in mind I did my first intent creating a neovim plugin that does exactly that and after few months using it I decided to port core logic to a cli tool easy to integrate with any code editor or terminal emulator so anybody interested can integrate it in his dev workflow.

# terms

Sandbox is a different way to take code notes and examples so from now on this doc I am going to use some terms that need definitions.

## idea

An idea is a self contain, one file, small code snippet or example that shows how to do something for example:

- how to configura logging module in python
- how to create a simple socket server in cpp
- how to deal with command line arguments in bash
- SOLID principles explanation in markdown

This ideas can be example but at the same time it is a sandbox, it is an environment ready for you to create new things, to test new ideas and exotic things and share it with your coleages.

## work idea

Is a new non saved idea, sandbox provides functionality to create a new work file where to start to create something fast, is up to you  to decide to store it or leave it, by default is not stored in your repository of ideas. This is because repository of ideas is somewhere you want to put something that will last and you will consult in the future not some kind of disaster that you tried to build a day without enough coffee.

Sandbox automates the creation of the file for an specific environment and the functionality to format it following a style guide and to execute it in the terminal. This functionallitiy is easy to use in the terminal but is easy to integrate in text editors as well.

## environment

An environment is the specific part of sandbox that knows how to deal with an specific programming language or knows how to do an specific thing, for example, at the moment sandbox have support for:

- **cpp**: builds, formats and executes cpp.
- **bash**: executes bash.
- **python**: style and execution.
- **markdown**: shows using Glow.
- **echo**: batcats any file.

More environments will be added in the future as well as a system for users to add their own environments without having to contribute to sandbox.

# installation

Sandbox is a pyproject tool, just build it and install .whl package:

```bash
pip install build

python3 -m build

pip install dist/*.whl --force-reinstall
```

# configuration

Defaults for sandbox are defined through environment variables, those defaults can be overridden through arguments but is handy to set it up:

```bash
export SANDBOX_IDEAS="path/to/your/ideas"
export SANDBOX_EDITOR="your favourite editor (neovim)"
```

## SANDBOX_IDEAS

This env variable points to your ideas folder, is where you are going to store all your ideas (code notes), it is a good idea to make it a git repository so you keep track of all changes done there and you can make it available in any machine you want.

## SANDBOX_EDITOR

Sandbox have a use case that allows to open for edition an idea, this env var set ups the default editor, if this variable is not set it fallsback to vim.

# usage

Once installed you will be able to run `sandbox` command, check it like this:

```bash
➜  sandbox --help
usage: sandbox [-h] [-i IDEAS] {reset,open,save,execute} ...

sandbox framework

positional arguments:
  {reset,open,save,execute}

optional arguments:
  -h, --help            show this help message and exit
  -i IDEAS, --ideas IDEAS
                        ideas repo path
```

Optional argument `-i` is to override env var `SANDBOX_IDEAS`.

Positional arguments are the different use cases:

- **reset**: creates a new work idea of an specific environment.
- **open**: opens idea in text editor.
- **execute**: executes idea.
- **save**: saves work idea in ideas folder.

Each use case have its own arguments and its own help you can check it like this:

```bash
sandbox execute --help
```

## reset

Any time you have a new idea run this command, this is going to create a new work idea of the environment of your selection:

```bash
➜  sandbox reset --help
usage: sandbox reset [-h] -e ENV [-o OUTPUT]

optional arguments:
  -h, --help            show this help message and exit
  -e ENV, --env ENV     environment to use
  -o OUTPUT, --output OUTPUT
                        output work file
```

arguments:
- env: an environment is the "language support" to use, the implementation that knows how to format, execute and generate a template of idea.
- output: work idea file path, by default it fallbacks to your ideas repository defined in `SANDBOX_IDEAS`.

```bash
# you can specify where you want it
sandbox reset -e cpp -o . # this is going to generate cpp hello world in ./main.cpp
sandbox reset -e python -o . # this is going to generate python hello world in ./main.py
sandbox reset -e markdown -o . # this is going to generate an empty markdown file in ./main.md
sandbox reset -e bash -o . # this is going to generate bash hello world in ./main.sh

# by default will use ideas path
sandbox reset -e cpp # this is going to generate cpp hello world in ${SANDBOX_IDEAS}/main.cpp

# if you specify the ideas path is going to use the overridden one
sandbox -i ~/example reset -e cpp # this is going to generate cpp hello world in ~/example/main.cpp
```

If you use reset where you already have a work idea this command is going to delete the previous one, remember that a work idea is a fast way to write an idea and if it works or have potential you should save it and keep working from ideas repo.

## open

Open idea on work editor:

```bash
➜  sandbox open --help
usage: sandbox open [-h] [-e EDITOR] [-p PATH]

optional arguments:
  -h, --help            show this help message and exit
  -e EDITOR, --editor EDITOR
                        editor to use
  -p PATH, --path PATH  idea or directory path
  -w, --work_idea       open current work idea
```

Without arguments sandbox will open fzf in `SANDBOX_IDEAS` to choose one.

arguments:
- editor: override `SANDBOX_EDITOR`.
- path: override `SANDBOX_IDEAS`, you can also specify a file path and it will open directly the file and not a work idea on this path.
- work_idea: directly open work idea.

```bash
sandbox open # this will display fzf on SANDBOX_IDEAS
sandbox -i ~/example open # this will pen fzf on ~/example
sandbox open -p ./main.cpp # this will open ./main.cpp
sandbox open -p ./ # this will open fzf in ./
sandbox open -w # this will open ${SANDBOX_IDEAS}/main*
sandbox -i ~/example -w # this will open ~/example/main*
```

## execute

An `idea` is code note, is a small self contained example of code like a Godbolt example, if it is self contained it can be executed by its own, an idea environment is the environment that knows how to execute this specific idea.

```bash
➜  sandbox execute --help
usage: sandbox execute [-h] [-p PATH] [-e ENV]

optional arguments:
  -h, --help            show this help message and exit
  -p PATH, --path PATH  work file or ideas directory
  -e ENV, --env ENV     force specific env regardless file meta
```

Without arguments sandbox will open fzf in `SANDBOX_IDEAS` to choose one.

arguments:
- path: path of specific idea or directory.
- env: by default is going to use idea environment written in idea metadata but you can force an specific environment if you want, it is not guarantee that is going to work.

```bash
sandbox execute # this will open fzf on `SANDBOX_IDEAS` and execute the chosen one
sandbox execute -p ./main.cpp # this will execute ./main.cpp
sandbox execute -p ~/example # this will open fzf on ~/example
sandbox -i ~/example execute # this will open fzf on ~/example
sandbox execute -p ./main.cpp -e echo # this will execute ./main.cpp forcing echo environment
sandbox execute -p ./main.cpp -e python # this will try to execute ./main.cpp with python environment (it is not going to work)
sandbox execute -e echo # this will open fzf on `SANDBOX_IDEAS` and execute the chosen one forcing echo env
```

## save

When you create a new idea and this shows that actually have some value you can store it in your `SANDBOX_IDEAS` folder.

```bash
➜  sandbox save --help
usage: sandbox save [-h] -p PATH

optional arguments:
  -h, --help            show this help message and exit
  -p PATH, --path PATH  work file
```

By default save command is going to save work idea under your `SANDBOX_IDEAS` dir.

You can override your ideas dir or you can specify it or a file with `-p`.

arguments:
- path: specify idea path or directory path.

```bash
sandbox save # save work idea under SANDBOX_IDEAS
sandbox -i ~/example save # save work idea under ~/example
sandbox save -p ~/example # save work idea under ~/example
sandbox save -p ./main.cpp # save ./main.cpp
```

To save sandbox is going to read idea metadata, specifically:
- sandbox_idea: this is the path in ideas folder where is going to be saved
- sandbox_name: this is the name of the idea file that is going to be saved

Example:

```cpp
// sandbox_idea: cpp/basics
// sandbox_name: for_loop
// sandbox_description: example of for loop
// sandbox_env: cpp
```

Run sandbox save on this file will place the file in:

```bash
${SANDBOX_IDEAS}/cpp/basics/for_loop.cpp
```

Realize that due execute and open uses fzf folder where to store idea acts as a search filter.
