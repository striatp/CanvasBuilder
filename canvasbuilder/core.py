from typing import Union, Tuple
from .Exceptions.WindowErrorHandling import WindowError # Importing the window error handler
from .Exceptions.CanvasErrorHandling import CanvasError # Importing the canvas error handler
from tkinter import Tk, Canvas as TkCanvas, CENTER

# Variable to track if the window is initialized
window_initialized = False

# Variable to track if the canvas is drawn
canvas_initialized = False

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
    """
    Convert an RGB tuple to a hexadecimal color string.

    Args:
        rgb (Tuple[int, int, int]): A tuple containing three integers representing the red, green, and blue values.

    Returns:
        str: A string representing the hexadecimal color (e.g., '#ff0000' for red).
    """
    return f'#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}'

# Window class to create the window
class Window:
    """
    A class to create a Tkinter window.

    Attributes:
        root (Tk): The main Tkinter window instance.
    """

    # Initializing the class
    def __init__(self, width: int = 800, height: int = 600, title: str = "My Canvas") -> None:
        """
        Initialize the Window instance.

        Args:
            width (int): The width of the window (default is 800).
            height (int): The height of the window (default is 600).
            title (str): The title of the window (default is "My Canvas").

        Raises:
            WindowError: If the window has already been initialized.
            ValueError: If width or height is not a positive integer or if title is not a string.
        """
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

    # Method to render the window
    def run(self) -> None:
        """
        Start the main loop for the Tkinter window to display it.

        This method should be called to make the window responsive.
        """
        self.root.mainloop()  

# Canvas class to create and append the canvas on the screen
class Canvas:
    """
    A class to create a Tkinter canvas.

    Attributes:
        canvas (TkCanvas): The Tkinter canvas instance.
    """

    # Initializing the class
    def __init__(self, window: Window, width: int, height: int, background_color: Union[str, Tuple[int, int, int]] = "white") -> None:
        """
        Initialize the Canvas instance.

        Args:
            window (Window): The Window instance to which the canvas will be attached.
            width (int): The width of the canvas.
            height (int): The height of the canvas.
            background_color (Union[str, Tuple[int, int, int]]): The background color of the canvas, 
                either as a string from the color map or an RGB tuple.

        Raises:
            WindowError: If a window has not been initialized.
            ValueError: If width or height is not a positive integer, if the background_color is not valid.
        """
        global canvas_initialized
        
        # Checking if the window wasn't initialized before
        if canvas_initialized:
            raise CanvasError("The canvas is already drawn.")

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
            self.background_color = background_color
        # Background color checks: tuple (convert to hex)
        elif isinstance(background_color, tuple):
            if len(background_color) == 3:
                for c in background_color:
                    if not 0 <= c <= 255:
                        raise ValueError("Each value in the 'background_color' tuple must be between 0 and 255.")
                self.background_color = rgb_to_hex(background_color)  # Convert tuple to hex
            else:
                raise ValueError("The 'background_color' argument must be a tuple of 3 integers.")

        # Access the root from the Window instance and create the canvas
        self.canvas = TkCanvas(window.root, width=width, height=height, bg=self.background_color)
        self.canvas.pack(anchor=CENTER, expand=True)
