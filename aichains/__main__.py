"""
Dojo for getting started.
"""
import IPython
import fire
import traitlets.config
from IPython.terminal.prompts import Prompts, Token
from dotenv import load_dotenv

from aichains import arxiv, chat


class MyPrompts(Prompts):
    def in_prompt_tokens(self):
        return [(Token.Prompt, '>> ',)]

    def out_prompt_tokens(self):
        return [(Token.Prompt, '<< ',)]


def repl():
    """Chat with chains interactively."""
    config = traitlets.config.Config()
    config.TerminalInteractiveShell.prompts_class = MyPrompts
    config.TerminalIPythonApp.exec_lines = [
        'from dotenv import load_dotenv; load_dotenv()',
        'from aichains import *',
    ]

    IPython.start_ipython(argv=[], config=config)


if __name__ == "__main__":
    load_dotenv()

    fire.Fire({
        'repl': repl,
        'arxiv': arxiv,
        'chat': chat
    })
