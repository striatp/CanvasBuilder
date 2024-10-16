from tkinter import Tk
from typing import Union

class Window:
  def __init__(self, width: int = 800, height: int = 600, title: str = "My Canvas"):
    root = Tk()
    root.geometry(f"{width}x{height}")
    root.title(title)

  def run(self):
    root.mainloop()
