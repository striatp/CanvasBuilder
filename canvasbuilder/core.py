from typing import Union, Tuple

class Canvas:
    def __init__(self, width: Union[int, str] = 400, height: Union[int, str] = 300, background_color: Union[str, Tuple[int, int, int]] = "white") -> None:
        # Validate width
        if isinstance(width, int):
            if width <= 0:
                raise ValueError("The 'width' argument must be a positive integer.")
        elif isinstance(width, str):
            if not width.endswith("px") or not width[:-2].isdigit() or int(width[:-2]) <= 0:
                raise ValueError("The 'width' argument must be a positive integer or a string ending with 'px' (e.g., '400px').")
        else:
            raise ValueError("The 'width' argument must be a positive integer or a string.")
        
        # Validate height
        if isinstance(height, int):
            if height <= 0:
                raise ValueError("The 'height' argument must be a positive integer.")
        elif isinstance(height, str):
            if not height.endswith("px") or not height[:-2].isdigit() or int(height[:-2]) <= 0:
                raise ValueError("The 'height' argument must be a positive integer or a string ending with 'px' (e.g., '300px').")
        else:
            raise ValueError("The 'height' argument must be a positive integer or a string.")
        
        # Assign the attributes
        self.width = width
        self.height = height
        self.background_color = background_color

# Example usage
canvas1 = Canvas(500, 300, "blue")      # Valid case with integers
canvas2 = Canvas("500px", "300px")      # Valid case with strings
