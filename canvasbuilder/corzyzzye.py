from typing import Union, Tuple
from tkinter import Tk, Canvas

class Canvas:
    def __init__(self, width: Union[int, str] = 400, height: Union[int, str] = 300, background_color: Union[str, Tuple[int, int, int]] = "white") -> None:
        # Validate width
        if isinstance(width, int):
            if width <= 0:
                raise ValueError("The 'width' argument must be a positive integer.")
        elif isinstance(width, str):
            if not width.endswith("px") or not width[:-2].isdigit() or int(width[:-2]) <= 0:
                raise ValueError("The 'width' argument must be a positive integer or a string ending with 'px' (e.g., '400px').")
            width = int(width[:-2])
        
        # Validate height
        if isinstance(height, int):
            if height <= 0:
                raise ValueError("The 'height' argument must be a positive integer.")
        elif isinstance(height, str):
            if not height.endswith("px") or not height[:-2].isdigit() or int(height[:-2]) <= 0:
                raise ValueError("The 'height' argument must be a positive integer or a string ending with 'px' (e.g., '300px').")
            height = int(height[:-2])
        
        self.width = width
        self.height = height
        self.background_color = background_color

    # Method to render the canvas
    def render(self):
        # Create a Tkinter window
        root = Tk()
        root.title("Canvas App")
        
        # Create the Canvas widget
        canvas = Canvas(root, width=self.width, height=self.height)
        canvas.pack()

        # Set the background color
        if isinstance(self.background_color, str):
            canvas.configure(bg=self.background_color)
        elif isinstance(self.background_color, tuple) and len(self.background_color) == 3:
            rgb_color = "#%02x%02x%02x" % self.background_color  # Convert RGB to hex
            canvas.configure(bg=rgb_color)
        
        # Start the Tkinter event loop
        root.mainloop()

# Example Usage
canvas_app = CanvasApp(500, 300, "blue")
canvas_app.render()
