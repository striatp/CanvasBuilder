import tkinter as tk

class MissingArgumentError(Exception):
    """Raised exception for missing arguments."""
    pass

# Core function
class CanvasWindow:
    def __init__(self):
        # Window and canvas are not initialized until init_canvas() is called
        self._initialized = False
        self.window = None
        self.canvas = None

    def init_canvas(self, title="Canvas App", width=600, height=400, bg="white"):
        """Initialize the main window and canvas"""
        self.window = tk.Tk()
        self.window.title(title)
        self.window.geometry(f"{width}x{height}")

        # Create and pack canvas
        self.canvas = tk.Canvas(self.window, width=width, height=height, bg=bg)
        self.canvas.pack()

        # Mark as initialized
        self._initialized = True

    def _check_init(self):
        """Check if canvas is initialized, raise error if not"""
        if not self._initialized:
            raise RuntimeError("Canvas not initialized! Please call init_canvas() before adding elements.")

    def draw_rectangle(self, x1, y1, x2, y2, fill="blue"):
        """Draw a rectangle on the canvas (only allowed after initialization)"""
        self._check_init()
        self.canvas.create_rectangle(x1, y1, x2, y2, fill=fill)

    def draw_circle(self, x, y, r, fill="red"):
        """Draw a circle on the canvas (only allowed after initialization)"""
        self._check_init()
        self.canvas.create_oval(x-r, y-r, x+r, y+r, fill=fill)

    def run(self):
        """Run the tkinter main loop (only after initialization)"""
        self._check_init()
        self.window.mainloop()
