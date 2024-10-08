# circle.py
from tkinter import Canvas  # Importing the Canvas class from tkinter for drawing
from .oval import Oval  # Importing the Oval class to inherit from
from .shape import ShapeError  # Importing custom ShapeError for exception handling

class Circle(Oval):
    def __init__(self, x, y, radius, color='black'):
        """
        Initializes a Circle instance.

        Args:
            x (int): The x-coordinate of the center of the circle.
            y (int): The y-coordinate of the center of the circle.
            radius (int): The radius of the circle.
            color (str): The color to fill the circle. Default is 'black'.
        """
        # Call the constructor of the Oval class, setting width and height to the diameter
        super().__init__(x, y, radius * 2, radius * 2, color)

    def draw(self, canvas: Canvas):
        """
        Draws the circle on the provided Tkinter canvas.

        Args:
            canvas (Canvas): The Tkinter canvas on which to draw the circle.
        """
        # Calculate the bounding box for the circle
        x0 = self.x - self.width / 2  # Top-left x-coordinate
        y0 = self.y - self.height / 2  # Top-left y-coordinate
        x1 = self.x + self.width / 2  # Bottom-right x-coordinate
        y1 = self.y + self.height / 2  # Bottom-right y-coordinate
        
        # Create the circle on the canvas using the bounding box
        canvas.create_oval(x0, y0, x1, y1, fill=self.color, outline=self.color)
      
