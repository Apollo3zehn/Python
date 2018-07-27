from math import pi
from typing import List

def ToggleCardinalDirectionPolar(polarCoordinates: List[float]):  
    return [polarCoordinates[0], ToggleCardinalDirection(polarCoordinates[1])]

def ToggleCardinalDirection(angle: float):  
    #       -angle + 360°   + 90°   mod 360°
    return (-angle + 2 * pi + pi / 2) % (2 * pi)
