from typing import Union
from tkinter import Canvas as TkCanvas, Tk

# Exception for missing arguments or invalid parameters
class MissingArgumentError(Exception):
    """Raised for missing arguments or invalid parameter inputs."""
    pass

# Main core class to initialize the canvas
class Create:
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
        # Argument validation
        if not isinstance(title, str):
            raise ValueError("The 'title' argument must be a string.")
        if not isinstance(width, int) or width <= 0:
            raise ValueError("The 'width' argument must be a positive integer.")
        if not isinstance(height, int) or height <= 0:
            raise ValueError("The 'height' argument must be a positive integer.")
        if not isinstance(background_color, (str, tuple)):
            raise ValueError("The 'background_color' argument must be a string (hex) or a tuple (RGB).")
        
        # Initialize the Tkinter root window
        self.root = Tk()
        self.root.title(title)  # Set the window title
        
        # Create the canvas and set the background color
        self.canvas = TkCanvas(self.root, width=width, height=height, bg=background_color)
        self.canvas.pack()  # Add the canvas to the root window
        
        # Track initialization state
        self._initialized = True
        
        # Store parameters for future use
        self.width = width
        self.height = height
        self.background_color = background_color

    def run(self) -> None:
        """
        Starts the Tkinter main loop to display the canvas window.

        Raises:
            RuntimeError: If the canvas is not initialized.
        """
        if self._initialized:
            self.root.mainloop()  # Start the Tkinter event loop
        else:
            raise RuntimeError("Canvas not initialized properly.")

    def breakCanvas(self) -> None:
        """
        Terminates the Tkinter main loop and closes the canvas window.

        Raises:
            RuntimeError: If the canvas is not initialized.
        """
        if self._initialized:
            self.root.destroy()  # Close the Tkinter window
        else:
            raise RuntimeError("Cannot break: Canvas not initialized.")

    def is_initialized(self) -> bool:
        """
        Returns the initialization status of the canvas.

        Returns:
            bool: True if the canvas is initialized, False otherwise.
        """
        return self._initialized
