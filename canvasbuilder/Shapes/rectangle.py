from ..core import Canvas
from typing import Union, Tuple
from ..Exceptions.CanvasErrorHandling import CanvasError

class Rectangle:
    def __init__(self, x: int = None, y: int = None, width: int = None, height: int = None, fill_color: Union[str, Tuple[int, int, int]]):
       if not Canvas.canvas_initialized:
           raise CanvasError("The canvas must be initialized before adding elements on it.")

      if not isinstance(x, int) or x == None:
          raise ValueError("The 'x' argument must be an integer.")
      if not isinstance(y, int) or y == None:
          raise ValueError("The 'y' argument must be an integer.")
      if not isinstance(width, int) or width == None or width <= 0:
          raise ValueError("The 'width' argument must be a positive integer.")
      if not isinstance(height, int) or height == None or height <= 0:
          raise ValueError("The 'height' argument must be a positive integer.")
      if not isinstance(fill_color, (str, tuple)):
          raise ValueError("The 'fill_color' argument must be a string or a tuple of 3 integers.")

      if isinstance(fill_color, str):
          if not fill_color in color_dictionary:
              raise 

    
    def draw(self):
        # Code to draw the rectangle

    def area(self):
        # Code to calculate the area

    def perimeter(self):
        # Code to calculate the perimeter

    def move(self):

    def resize(self):

    def set_fill_color(self):

    def set_outline_color(self):

    def set_outline_width(self):
