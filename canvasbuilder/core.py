from typing import Union, Tuple

class Canvas:
  def __init__(self, width: Union[int, str] = 400, height: Union[int, str] = 300, background_color: Union[str, Tuple[int, int, int]] = "white") -> None:
    if not isinstance(width, (int, str)) or width <= 0:
      raise ValueError("The 'width' argument must be a positive integer or a string.")
    if not isinstance(height, (int, str)) or height <= 0:
      raise ValueError("The 'height' argument must be a positive integer or a string.")
