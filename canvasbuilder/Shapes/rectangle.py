from ..core import Canvas
from ..Exceptions.CanvasErrorHandling import CanvasError

class Rectangle:
  
    def __init__(self, canvas: Canvas, x1: int, y1: int, x2: int, y2: int, color: str = "black") -> None:
        # Type checks and errors handling
        if not isinstance(x1, int) or not isinstance(y1, int) or not isinstance(x2, int) or not isinstance(y2, int):
            raise ValueError("Coordinates (x1, y1, x2, y2) must be integers.")
        if not isinstance(color, str):
            raise ValueError("Color must be a string.")

        self.canvas = canvas.canvas  # Access the canvas instance
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.color = color

        # Draw the rectangle on the canvas
        self.canvas.create_rectangle(x1, y1, x2, y2, fill=color)
