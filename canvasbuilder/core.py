from typing import Union

# Custom exception for error in the canvas initialization
class InitError(Exception):
  """Raised error for initialization errors."""
  pass

# Variable to know if the canvas is initialized
is_canvas_initialized = False
default_background_color = (255, 255, 255)

# Main class needed to create the canvas
class Canvas():
  def __init__(self, width: Union[int, str], height: Union[int, str], background_color: Union[str, tuple]):

async def PassFunc():
  pass # pass
