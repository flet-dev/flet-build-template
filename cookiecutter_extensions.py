from jinja2 import pass_context
from jinja2.ext import Extension


class FoobarExtension(Extension):
    def __init__(self, environment):
        super(FoobarExtension, self).__init__(environment)
        environment.filters["foobar"] = lambda v: v * 2
        environment.globals["get_pyproject"] = self.get_pyproject

    @pass_context
    def get_pyproject(self, context, setting):
        pyproject = context.get("pyproject", {})
        return f"Hello, {setting}! (pyproject: {pyproject})"
