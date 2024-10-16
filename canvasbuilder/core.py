from tkinter import Tk

class Window:
  def __init__(self, width: int = 800, height: int = 600, title: str = "My Canvas"):
    self.root = Tk()
    self.root.geometry(f"{width}x{height}")
    self.root.title(title)

  def run(self):
    self.root.mainloop()
