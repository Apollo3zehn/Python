import cmath
import math
from typing import Tuple, List

import pytest

from S1_Framework import Converter
from S1_Framework.IEC_61400_12.SiteAssessment.BaseTypes import (DisturbedObject,
                                                                ObstacleBase,
                                                                Sector)

class TestDisturbedObject(DisturbedObject):
    def GetEquivalentRotorDiameter(self, obstacle: ObstacleBase):
        pass

def PrepareData(polarCoordinates: Tuple[float, float]):

    referenceHeight: float
    wtgWmeDistance: float
    relativePosition: complex
    polarCoordinatesRadian: Tuple[float, float]
    polarCoordinatesNonCardinal: Tuple[float, float]
    validSectorSet: List[Sector]

    referenceHeight = 100
    wtgWmeDistance = 100

    polarCoordinatesRadian = (polarCoordinates[0], math.radians(polarCoordinates[1]))
    polarCoordinatesNonCardinal = Converter.ToggleCardinalDirectionPolar(polarCoordinatesRadian)
    relativePosition = cmath.rect(polarCoordinatesNonCardinal[0], polarCoordinatesNonCardinal[1])

    validSectorSet = [Sector.FromBoundaries(math.radians(50), math.radians(-50))]

    return (TestDisturbedObject(), relativePosition, referenceHeight, wtgWmeDistance, validSectorSet)

@pytest.mark.parametrize("polarCoordinates, obstacleHeight", [((199, 9), 34), ((200, 270), 67), ((400, 270), 100), ((800, 270), 134), ((200, 11), 67)])
def ShouldAcceptSignificanceOfObstacleTest(polarCoordinates: Tuple[float, float], obstacleHeight: float):

    (disturbedObject, relativePosition, referenceHeight, wtgWmeDistance, validSectorSet) = PrepareData(polarCoordinates)

    assert disturbedObject.IsObstacleSignificant(obstacleHeight, relativePosition, referenceHeight, wtgWmeDistance, validSectorSet)

@pytest.mark.parametrize("polarCoordinates, obstacleHeight", [((199, 9), 32), ((200, 270), 65), ((400, 270), 99), ((800, 270), 132)])
def ShouldDenySignificanceOfObstacleDueToHeightTest(polarCoordinates: Tuple[float, float], obstacleHeight: float):

    (disturbedObject, relativePosition, referenceHeight, wtgWmeDistance, validSectorSet) = PrepareData(polarCoordinates)

    assert not disturbedObject.IsObstacleSignificant(obstacleHeight, relativePosition, referenceHeight, wtgWmeDistance, validSectorSet)

@pytest.mark.parametrize("polarCoordinates, obstacleHeight", [((200, 9), 1e12)])
def ShouldDenySignificanceOfObstacleDueToLocationTest(polarCoordinates: Tuple[float, float], obstacleHeight: float):

    (disturbedObject, relativePosition, referenceHeight, wtgWmeDistance, validSectorSet) = PrepareData(polarCoordinates)

    assert not disturbedObject.IsObstacleSignificant(obstacleHeight, relativePosition, referenceHeight, wtgWmeDistance, validSectorSet)

@pytest.mark.parametrize("relativeDistance, expectedWidth", [(0.1, 100), (2, 100), (3, 67.8740945), (12, 35.625829), (20, 29.9891266), (20.1, 0)])
def ShouldCreateSectorTest(relativeDistance: float, expectedWidth: float):

    disturbedObject = TestDisturbedObject()
    location = 100+0j
    sector = disturbedObject.ToSector(location, 100 / relativeDistance)

    assert math.isclose(sector.Direction, math.radians(90), rel_tol=1e-3) and \
           math.isclose(sector.Width, math.radians(expectedWidth), rel_tol=1e-3)