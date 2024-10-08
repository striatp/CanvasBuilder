# arc.py
from tkinter import Canvas
from .shape import Shape, ShapeError

class Arc(Shape):
    """Class representing an arc shape.

    Attributes:
        width (float): Width of the bounding box of the arc.
        height (float): Height of the bounding box of the arc.
        start (float): Starting angle of the arc.
        extent (float): Extent angle of the arc.
    """

    def __init__(self, x: float, y: float, width: float, height: float, start: float, extent: float, color: str):
        """Initialize an arc with position, dimensions, and color.

        Args:
            x (float): X-coordinate of the bounding box.
            y (float): Y-coordinate of the bounding box.
            width (float): Width of the arc.
            height (float): Height of the arc.
            start (float): Starting angle of the arc.
            extent (float): Extent angle of the arc.
            color (str): Color of the arc.

        Raises:
            ShapeError: If width or height is not positive.
        """
        super().__init__(x, y, color)
        if width <= 0 or height <= 0:
            raise ShapeError("Width and height must be positive numbers.")
        self.width = width
        self.height = height
        self.start = start
        self.extent = extent

    def draw(self, canvas):
        """Draw the arc on the provided canvas."""
        canvas.create_arc(self.x, self.y, self.x + self.width, self.y + self.height, start=self.start, extent=self.extent, fill=self.color)
      
