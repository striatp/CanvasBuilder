# Importing shape classes to make them available at the package level
from .arc import Arc
from .circle import Circle
from .line import Line
from .oval import Oval
from .rectangle import Rectangle
from .square import Square
from .text import Text

# Public API accessibility
__all__ = ['Arc', 'Circle', 'Line', 'Oval', 'Rectangle', 'Square', 'Text']
