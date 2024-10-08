# line.py
from .shape import Shape, ShapeError

class Line(Shape):
    """Class representing a line shape.

    Attributes:
        x1 (float): Starting x-coordinate of the line.
        y1 (float): Starting y-coordinate of the line.
        x2 (float): Ending x-coordinate of the line.
        y2 (float): Ending y-coordinate of the line.
    """

    def __init__(self, x1: float, y1: float, x2: float, y2: float, color: str):
        """Initialize a line with start and end coordinates and color.

        Args:
            x1 (float): Starting x-coordinate.
            y1 (float): Starting y-coordinate.
            x2 (float): Ending x-coordinate.
            y2 (float): Ending y-coordinate.
            color (str): Color of the line.

        Raises:
            ShapeError: If any coordinate is not a valid number.
        """
        super().__init__(x1, y1, color)
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def draw(self, canvas):
        """Draw the line on the provided canvas."""
        canvas.create_line(self.x1, self.y1, self.x2, self.y2, fill=self.color)
