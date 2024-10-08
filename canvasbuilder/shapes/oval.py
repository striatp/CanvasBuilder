# oval.py
from tkinter import Canvas
from .shape import Shape, ShapeError

class Oval(Shape):
    """Class representing an oval shape.

    Attributes:
        width (float): Width of the bounding box of the oval.
        height (float): Height of the bounding box of the oval.
    """

    def __init__(self, x: float, y: float, width: float, height: float, color: str):
        """Initialize an oval with position, width, height, and color.

        Args:
            x (float): X-coordinate of the bounding box.
            y (float): Y-coordinate of the bounding box.
            width (float): Width of the oval.
            height (float): Height of the oval.
            color (str): Color of the oval.

        Raises:
            ShapeError: If width or height is not positive.
        """
        super().__init__(x, y, color)
        if width <= 0 or height <= 0:
            raise ShapeError("Width and height must be positive numbers.")
        self.width = width
        self.height = height

    def draw(self, canvas):
        """Draw the oval on the provided canvas."""
        canvas.create_oval(self.x, self.y, self.x + self.width, self.y + self.height, fill=self.color)
      
