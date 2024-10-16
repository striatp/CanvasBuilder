from typing import Union, Tuple
from .ErrorsHandler import WindowError # Importing the errors handlers
from tkinter import Tk, Canvas as TkCanvas, CENTER

# Variable to track if the window is initialized
window_initialized = False

# Color map
color_map = {
    "blue",
    "red",
    "green",
    "yellow",
    "brown",
    "black",
    "white",
    "orange",
    "purple",
    "gray"
}

# Window class to create the window
class Window:
    # Initializing the class
    def __init__(self, width: int = 800, height: int = 600, title: str = "My Canvas") -> None:
        global window_initialized
        
        # Checking if the window wasn't initialized before
        if window_initialized:
            raise WindowError("The window is already initialized.")
        
        # Type checks and errors handling
        if not isinstance(width, int) or width <= 0:
            raise ValueError("The 'width' argument must be a positive integer.")
        if not isinstance(height, int) or height <= 0:
            raise ValueError("The 'height' argument must be a positive integer.")
        if not isinstance(title, str):
            raise ValueError("The 'title' argument must be a string.")

        # Initializing the window
        self.root = Tk() # Initialize the Tk window
        self.root.geometry(f"{width}x{height}")
        self.root.title(title)
        
        # Makes sure the window variable is now on True, which prevents another window initialization
        window_initialized = True

    # Method to display the window
    def run(self) -> None:
        # Start the main loop for the window
        self.root.mainloop()  

# Canvas class to create and append the canvas on the screen
class Canvas:
    # Initializing the class
    def __init__(self, window: Window, width: int, height: int, background_color: Union[str, Tuple[int, int, int]]) -> None:
        # Checks if the window is initialized
        if not window_initialized:
            raise WindowError("A window must be initialized before the canvas.")

        # Type checks and errors handling
        if not isinstance(width, int) or width <= 0:
            raise ValueError("The 'width' argument must be a positive integer.")
        if not isinstance(height, int) or height <= 0:
            raise ValueError("The 'height' argument must be a positive integer.")
        # Background color checks
        if isinstance(background_color, str):
            if not background_color in color_map:
                raise ValueError(f"The 'background_color' argument must be a tuple or a string equal to one of the set of colors: {", ".join(color_map)}")

        # raise ValueError("The 'background' argument must be a string or a tuple.")

        # Access the root from the Window instance
        self.canvas = TkCanvas(window.root, width=width, height=height, bg=background_color)
        self.canvas.pack(anchor=CENTER, expand=True)
