from typing import Union, Tuple

class Canvas:
  def __init__(self, width: int = 400, height: int = 300, background_color: Union[str, Tuple[int, int, int]] = "white") -> None:
    if not isinstance(width, int) or width <= 0:
      raise ValueError("The 'width' argument must be a positive integer.")
    if not isinstance(height, int) or height <= 0:
      raise ValueError("The 'height' argument must be a positive integer.")
