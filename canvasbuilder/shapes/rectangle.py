# rectangle.py
from tkinter import Canvas
from .shape import Shape, ShapeError

class Rectangle(Shape):
    """Class representing a rectangle shape.

    Attributes:
        width (float): Width of the rectangle.
        height (float): Height of the rectangle.
    """

    def __init__(self, x: float, y: float, width: float, height: float, color: str):
        """Initialize a rectangle with position, width, height, and color.

        Args:
            x (float): X-coordinate of the top-left corner.
            y (float): Y-coordinate of the top-left corner.
            width (float): Width of the rectangle.
            height (float): Height of the rectangle.
            color (str): Color of the rectangle.

        Raises:
            ShapeError: If width or height is not positive.
        """
        super().__init__(x, y, color)
        if width <= 0 or height <= 0:
            raise ShapeError("Width and height must be positive numbers.")
        self.width = width
        self.height = height

    def draw(self, canvas):
        """Draw the rectangle on the provided canvas."""
        canvas.create_rectangle(self.x, self.y, self.x + self.width, self.y + self.height, fill=self.color)
      
