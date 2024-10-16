# canvasbuilder/__init__.py

# Importing the main classes and functions
from .core import Window, Canvas, rgb_to_hex
from .Exceptions.WindowErrorHandling import WindowError

# Available ressources for the public API
__all__ = [
    "Window",
    "Canvas",
    "rgb_to_hex",
    "WindowError"
]
