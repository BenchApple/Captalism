# Benjamin Chappell

from enum import Enum, auto

# Stores the position of each player
class Position(Enum):
    PRES = 0
    VICE_PRES = auto()
    UPPER_MID = auto()
    LOWER_MID = auto()
    VICE_SCUM = auto()
    SCUM = auto()
