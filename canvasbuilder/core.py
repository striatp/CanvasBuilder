from tkinter import Tk, Canvas as TkCanvas, CENTER

window_initialized = False

class Window:
    def __init__(self, width: int = 800, height: int = 600, title: str = "My Canvas"):
        global window_initialized
        self.root = Tk()  # Initialize the Tk window
        self.root.geometry(f"{width}x{height}")
        self.root.title(title)
        window_initialized = True

    def run(self):
        self.root.mainloop()  # Start the main loop for the window

class Canvas:
    def __init__(self, window: Window, width: int, height: int, background_color: str, position: str = 'center'):
        if not window_initialized:
            raise WindowError("A window must be initialized before the canvas.")
        
        # Access the root from the Window instance
        self.canvas = TkCanvas(window.root, width=width, height=height, bg=background_color, anchor=CENTER)
        
        # Pack or place the canvas based on the provided position (can be expanded to include position handling)
        self.canvas.pack()
