import functools

from aichains.render import RenderType, render_data

DEFAULT_OUTPUT_CONFIG = dict(
    render=True,
    render_type=RenderType.Markdown,
    render_kwargs=dict(),
)


def config_render(**kwargs):
    DEFAULT_OUTPUT_CONFIG.update(kwargs)


def render_output(f):
    """
    Decorator to render output of a function.
    """
    defaults = DEFAULT_OUTPUT_CONFIG

    @functools.wraps(f)
    def fn(*args, render=None, render_type=None, render_kwargs=None, **kwargs):
        render = render or defaults.get('render')
        render_type = render_type or defaults.get('render_type')
        render_kwargs = render_kwargs or defaults.get('render_kwargs')

        result = f(*args, **kwargs)
        if not render:
            return result

        render_data(result, render_type=render_type, **render_kwargs)
        return

    return fn
