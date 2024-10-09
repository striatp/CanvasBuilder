from typing import Union
from tkinter import Canvas as TkCanvas, Tk

# Execption for missing arguments or invalid params
class MissingArgumentError(Exception):
    """Raised exception for missing arguments or invalid params inputs"""
    pass

# Set the default initialization to false
is_initialized = False

# Main core class to initialize the canvas
class Create():
    def __init__(self, title: str = "My Canvas", width: int = 300, height: int = 300, background_color: Union[str, tuple] = "white") -> None:
        """
        Initializes a new Tkinter window and canvas with the given parameters.

        Args:
            title (str): The window title.
            width (int): The width of the canvas.
            height (int): The height of the canvas.
            background_color (Union[str, tuple]): The background color of the canvas (hex string or tuple).
        
        Raises:
            ValueError: If invalid types or values are provided for any argument.
        """

        # Argument validation and error handling
        if not isinstance(title, str):
            raise ValueError("The 'title' argument must be a string.")
        if not isinstance(width, int) or width <= 0:
            raise ValueError("The 'width' argument must be a positive integer.")
        if not isinstance(height, int) or height <= 0:
            raise ValueError("The 'height' argument must be a positive integer.")
        if not isinstance(background_color, (str, tuple)):
            raise ValueError("The 'background_color' argument must be a string (hex) or a tuple (RGB).")
        
        # Tkinter window and canvas setup
        self.root = Tk()  # Create the root window
        self.root.title(title)  # Set window title
        self.canvas = TkCanvas(self.root, width=width, height=height, bg=background_color)  # Create canvas
        self.canvas.pack()  # Add the canvas to the window

        # Set instance variables and mark as initialized
        global is_initialized
        is_initialized = True
        self.width = width
        self.height = height
        self.background_color = background_color
    
    # Display the empty canvas on the screen
    def run(self):
        """
        Starts the Tkinter main loop to display the canvas window.
        
        Raises:
            RuntimeError: If the canvas is not initialized.
        """
        if self._initialized:
            self.root.mainloop()  # Start Tkinter event loop
        else:
            raise RuntimeError("Canvas not initialized properly.")

    # Closes the canvas
    def breakCanvas(self):
        """
        Terminates the Tkinter main loop and closes the canvas window.

        Raises:
            RuntimeError: If the canvas is not initialized.
        """
        if self._initialized:
            self.root.destroy()  # Destroy the Tkinter window and stop the main loop
        else:
            raise RuntimeError("Cannot break: Canvas not initialized.")

# Function to check if the canvas has been initialized
def initialized(self) -> bool:
    """
    Returns the initialization status of the canvas.

    Returns:
        bool: True if the canvas is initialized, False otherwise.
    """
    return True if is_initialized else False
