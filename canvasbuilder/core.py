from tkinter import Canvas, Tk
from typing import Union

# Missing argument custom error
class MissingArgumentError(Exception):
    """Raised exception for missing arguments."""
    pass

# Window initialization
class Canvas():
    def __init__(self, title: str = "My Canvas", width: int = 500, height: int = 800, background_color: Union[str, tuple]) -> None:

        self._initialized = False
        
        # Type checks
        if not isinstance(title, str):
            raise ValueError("The 'title' argument must be a string.")

        if not isinstance(width, int):
            raise ValueError("The 'width' argument must be an integer.")
        if width <= 0:
            raise ValueError("The 'width' argument must be a positive integer.")

        if not isinstance(height, int):
            raise ValueError("The 'height' argument must be an integer.")
        if height <= 0:
            raise ValueError("The 'height' argument must be a positive integer.")

        if not isinstance(background_color, Union[str, tuple]):
            raise ValueError("The 'background_color' argument must be a string or a tuple.")

        self.root = Tk()
        self.root.title(title)
        self.canvas = Canvas(self.root, width=width, height=height, bg=background_color)
        self._initialized = True
        self.width = width
        self.height = height
        self.background_color = background_color

    def initialized(self):
        return True if self._initialized else False
