from typing import Union, Tuple
from .ErrorsHandler import WindowError  # Importing the errors handlers
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

# Function to convert RGB tuple to hexadecimal string
def rgb_to_hex(rgb: Tuple[int, int, int]) -> str:
    return f'#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}'

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
        self.root = Tk()  # Initialize the Tk window
        self.root.geometry(f"{width}x{height}")
        self.root.title(title)
        
        # Prevents another window initialization
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

        # Background color checks: string
        if isinstance(background_color, str):
            if background_color not in color_map:
                raise ValueError(f"The 'background_color' argument must be one of: {', '.join(color_map)}")
        # Background color checks: tuple (convert to hex)
        elif isinstance(background_color, tuple):
            if len(background_color) == 3:
                for c in background_color:
                    if not 0 <= c <= 255:
                        raise ValueError("Each value in the 'background_color' tuple must be between 0 and 255.")
                self.background = rgb_to_hex(background_color)  # Convert tuple to hex
            else:
                raise ValueError("The 'background_color' argument must be a tuple of 3 integers.")

        # Access the root from the Window instance and create the canvas
        self.canvas = TkCanvas(window.root, width=width, height=height, bg=self.background_color)
        self.canvas.pack(anchor=CENTER, expand=True)
