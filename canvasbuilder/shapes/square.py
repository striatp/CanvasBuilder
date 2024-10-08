# square.py
from .shape import Shape, ShapeError

class Square(Shape):
    def __init__(self, x: float, y: float, size: float, color: str):
        super().__init__(x, y, color)
        if size <= 0:
            raise ShapeError("Size must be a positive number.")
        self.size = size

    def draw(self, canvas):
        """Draw the square on the provided canvas.

        Args:
            canvas: The canvas object on which to draw the square.
        """
        # Create a rectangle representing the square
        canvas.create_rectangle(
            self.x,
            self.y,
            self.x + self.size,
            self.y + self.size,
            fill=self.color
        )
