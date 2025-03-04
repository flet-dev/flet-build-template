from typing import Any, Optional

import cookiecutter.utils


def get_pyproject(pyproject_toml: Any, setting: Optional[str] = None):
    if not setting:
        return pyproject_toml

    d = pyproject_toml
    for k in setting.split("."):
        d = d.get(k)
        if d is None:
            return None
    return d


def my_custom_function(value):
    """Example function: returns the value in uppercase"""
    return value.upper()


def another_function(value1, value2):
    """Concatenates two values with a space"""
    return f"{value1} {value2}"


# Inject custom functions into Jinja's global context
def add_custom_filters(cookiecutter):
    cookiecutter.globals["my_custom_function"] = my_custom_function
    cookiecutter.globals["another_function"] = another_function


# Run after project is generated
add_custom_filters(cookiecutter)
