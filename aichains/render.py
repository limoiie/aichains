import enum

from rich.console import Console
from rich.markdown import Markdown

console = Console()


class RenderType(enum.Enum):
    Normal = 0
    Pretty = 1
    Markdown = 2


def render_data(*objects, render_type: RenderType, **kwargs):
    if render_type is RenderType.Markdown:
        render_markdown(*objects, **kwargs)

    elif render_type is RenderType.Pretty:
        render_pretty(*objects, **kwargs)

    else:
        render_normal(*objects, **kwargs)


def render_normal(*objects: object, **kwargs):
    print(*objects, **kwargs)


def render_pretty(*objects: object, **kwargs):
    console.print(*objects, **kwargs)


def render_markdown(*objects: object, sep='\n\n', **kwargs):
    content = sep.join(map(str, objects))
    kwargs.setdefault('code_theme', 'one-dark')
    console.print(Markdown(content, **kwargs))
