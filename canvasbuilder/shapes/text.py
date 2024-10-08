# text.py
from tkinter import Canvas
from .shape import Shape, ShapeError

class Text(Shape):
    """Class representing a text shape.

    Attributes:
        text (str): The text to be drawn.
        font (str): The font of the text.
    """

    def __init__(self, x: float, y: float, text: str, font: str, color: str):
        """Initialize text with position, content, font, and color.

        Args:
            x (float): X-coordinate of the text.
            y (float): Y-coordinate of the text.
            text (str): The text to be drawn.
            font (str): The font of the text.
            color (str): Color of the text.

        Raises:
            ShapeError: If text or font is not a valid string.
        """
        super().__init__(x, y, color)
        self.text = text
        self.font = font

    def draw(self, canvas):
        """Draw the text on the provided canvas."""
        canvas.create_text(self.x, self.y, text=self.text, font=self.font, fill=self.color)
      
