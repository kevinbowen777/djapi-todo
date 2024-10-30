"""Sphinx configuration."""

project = "djapi-todo"
author = "Kevin Bowen"
copyright = f"2024, {author}"
#
html_theme = "furo"
html_logo = "django_24.png"
html_title = "djapi-todo"
extensions = [
    "sphinx.ext.duration",
]
