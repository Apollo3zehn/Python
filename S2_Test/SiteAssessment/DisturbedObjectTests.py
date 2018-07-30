import cmath
import math
from typing import Dict, Tuple

import pytest

from S1_Framework import Converter
from S1_Framework.IEC_61400_12.SiteAssessment.BaseTypes import (DisturbedObject,
                                                                ObstacleBase,
                                                                Sector)


class TestDisturbedObject(DisturbedObject):
    def FindDisturbedSectors(self, obstacleToLocationMap: Dict[ObstacleBase, complex]):
        pass

# def CreateSmallWtgObstacle():

#     wtgObstacle = WtgObstacle()

#     WtgObstacle.HubHeight = 90
#     WtgObstacle.InOperation = True
#     WtgObstacle.IsSmall = True
#     WtgObstacle.RotorDiameter = 20
#     WtgObstacle.TowerBaseDiameter = 4

#     return wtgObstacle

def PrepareData(polarCoordinates: Tuple[float, float]):

    referenceHeight: float
    wtgWmeDistance: float
    relativePosition: complex
    polarCoordinatesRadian: Tuple[float, float]
    polarCoordinatesNonCardinal: Tuple[float, float]

    referenceHeight = 100
    wtgWmeDistance = 100
    polarCoordinatesRadian = (polarCoordinates[0], math.radians(polarCoordinates[1]))
    polarCoordinatesNonCardinal = Converter.ToggleCardinalDirectionPolar(polarCoordinatesRadian)

    relativePosition = cmath.rect(polarCoordinatesNonCardinal[0], polarCoordinatesNonCardinal[1])

    return (TestDisturbedObject(), relativePosition, referenceHeight, wtgWmeDistance)

@pytest.mark.parametrize("polarCoordinates, obstacleHeight", [((199, 9), 34), ((200, 270), 67), ((400, 270), 100), ((800, 270), 134), ((200, 11), 67)])
def ShouldAcceptSignificanceOfWtgObstacleTest(polarCoordinates: Tuple[float, float], obstacleHeight: float):

    (disturbedObject, relativePosition, referenceHeight, wtgWmeDistance) = PrepareData(polarCoordinates)
    disturbedSectorSet = [Sector.FromBoundaries(math.radians(-50), math.radians(50))]

    assert disturbedObject.IsObstacleSignificant(obstacleHeight, relativePosition, referenceHeight, wtgWmeDistance, disturbedSectorSet)

@pytest.mark.parametrize("polarCoordinates, obstacleHeight", [((199, 9), 32), ((200, 270), 65), ((400, 270), 99), ((800, 270), 132)])
def ShouldDenySignificanceOfWtgObstacleDueToHeightTest(polarCoordinates: Tuple[float, float], obstacleHeight: float):

    (disturbedObject, relativePosition, referenceHeight, wtgWmeDistance) = PrepareData(polarCoordinates)
    disturbedSectorSet = [Sector.FromBoundaries(math.radians(-50), math.radians(50))]

    assert not disturbedObject.IsObstacleSignificant(obstacleHeight, relativePosition, referenceHeight, wtgWmeDistance, disturbedSectorSet)

@pytest.mark.parametrize("polarCoordinates, obstacleHeight", [((200, 0), 1e12)])
def ShouldDenySignificanceOfWtgObstacleDueToLocationTest(polarCoordinates: Tuple[float, float], obstacleHeight: float):

    (disturbedObject, relativePosition, referenceHeight, wtgWmeDistance) = PrepareData(polarCoordinates)
    disturbedSectorSet = [Sector.FromBoundaries(math.radians(-50), math.radians(50))]

    assert not disturbedObject.IsObstacleSignificant(obstacleHeight, relativePosition, referenceHeight, wtgWmeDistance, disturbedSectorSet)
