from tkinter import Tk

window_initialized = False
canvas_initialized = True

class Window:
  def __init__(self, width: int = 800, height: int = 600, title: str = "My Canvas"):
    global window_initialized
    
    self.root = Tk()
    self.root.geometry(f"{width}x{height}")
    self.root.title(title)

    window_initialized = True

  def run(self):
    self.root.mainloop()

class Canvas:
  def __init__(self, width, height, background_color, position):
    if not window_initialized:
      raise WindowError("a window not init")
      
