# Aichains

Aichains contains demos of Langchain.

## Installation

If you don't have it already, install Poetry:

``` shell
pip install poetry
```

To prepare a Python venv via Poetry:

``` shell
# Create a new Python venv with Python 3.9
poetry env use 3.9
# Or use an existing interpreter via Poetry use:
# poetry env use /full/path/to/an/existing/python3.9
```

Activate the virtual environment, then install all the dependencies and the project:

``` shell
# Activate the environment
poetry shell
# Install the dependencies and the project
poetry install
```

## Usage

You can chat with ChatGPT like this:

```shell
python -m aichain chat --question='What is OpenAI API?'
```

You can also chat with arXiv:

```shell
python -m aichain arxiv --question='Give me a list of papers about binary code analysis'
```

Or, you can start an interactive shell similar to IPython:

```shell
python -m aichain repl
```

In the shell, you can use the `chat` and `arxiv` functions:

-  `chat(question='question about anything')` for ChatGPT-like functionality
-  `arxiv(question='research on arxiv')` to query information from arXiv

For full usages, please run command with `--help` options:

```shell
python -m aichain -- --help
python -m aichain chat -- --help
python -m aichain arxiv -- --help
python -m aichain repl -- --help
```
