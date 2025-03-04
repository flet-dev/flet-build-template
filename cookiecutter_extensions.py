from jinja2.ext import Extension


class FoobarExtension(Extension):
    def __init__(self, environment):
        super(FoobarExtension, self).__init__(environment)
        environment.filters["foobar"] = lambda v: v * 2
        environment.globals["greet"] = lambda name: f"Hello, {name}"
