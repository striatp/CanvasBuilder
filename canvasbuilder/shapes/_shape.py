from ../core import initialized

class ShapeError(Exception):
    """Custom exception for shape-related errors."""
    pass

class Shape:
    """Base class for all shapes.

    Attributes:
        x (float): The x-coordinate of the shape.
        y (float): The y-coordinate of the shape.
        color (str): The color of the shape, defined as a string.
    """

    def __init__(self, x: float, y: float, color: str):
        """Initialize a shape with position and color.

        Args:
            x (float): The x-coordinate of the shape.
            y (float): The y-coordinate of the shape.
            color (str): The color of the shape.

        Raises:
            ShapeError: If the color is not a valid string.
        """
        
        if not initialized:
            raise ShapeError("") # init error
        
        self.x = x
        self.y = y
        self.color = color

        # Validate the color format
        if not isinstance(color, str):
            raise ShapeError("Color must be a string representing the color name or hex code.")

    def draw(self, canvas):
        """Draw the shape on the provided canvas.

        Args:
            canvas: The canvas object on which to draw the shape.

        Raises:
            NotImplementedError: This method should be implemented by subclasses.
        """
        raise NotImplementedError("This method should be implemented by subclasses.")
