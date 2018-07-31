import math

def ShortestAngularDistance(angle1: float, angle2: float):  
    return math.atan2(math.sin(angle1 - angle2), math.cos(angle1 - angle2))
