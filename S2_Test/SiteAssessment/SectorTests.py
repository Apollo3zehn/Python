import math
import pytest

from S1_Framework.IEC_61400_12.SiteAssessment.BaseTypes import Sector

@pytest.mark.parametrize("angle", [0, 90, 180, 270, 360, 900, -900])
def ShouldNotContainAngleTest(angle: float):
    sector = Sector.FromDirection(math.radians(45), math.radians(20))
    assert not sector.Contains(math.radians(angle))

@pytest.mark.parametrize("angle", [-10, -150, 0, 110])
def ShouldContainAngleTest(angle: float):
    sector = Sector.FromDirection(math.radians(-20), math.radians(280))
    assert sector.Contains(math.radians(angle))

@pytest.mark.parametrize("angle", [-1, 0, 1])
def ShouldContainAngleAroundZeroDegreesTest(angle: float):
    sector = Sector.FromDirection(math.radians(0), math.radians(10))
    assert sector.Contains(math.radians(angle))

@pytest.mark.parametrize("angle", [179, 180, 181])
def ShouldContainAngleAround180DegreesTest(angle: float):
    sector = Sector.FromDirection(math.radians(180), math.radians(10))
    assert sector.Contains(math.radians(angle))

def ShouldContainExcludeAngleAtLowerBoundTest():
    sector = Sector.FromDirection(math.radians(0), math.radians(10))
    assert sector.Contains(math.radians(-5))

def ShouldNotContainAngleAtUpperBoundTest():
    sector = Sector.FromDirection(math.radians(0), math.radians(10))
    assert not sector.Contains(math.radians(5))

@pytest.mark.parametrize("direction, width, expectedMinDirection, expectedMaxDirection", [(0, 20, 350, 10), (-50, 180, 220, 40), (270, 180, 180, 0)])
def ShouldCalculateMinDirectionTest(direction: float, width: float, expectedMinDirection: float, expectedMaxDirection: float):
    sector = Sector.FromDirection(math.radians(direction), math.radians(width))
    assert math.isclose(sector.Min, math.radians(expectedMinDirection), rel_tol=1e-6) and \
           math.isclose(sector.Max, math.radians(expectedMaxDirection), rel_tol=1e-6)

@pytest.mark.parametrize("minDirection, maxDirection, expectedDirection, expectedWidth", [
    (-5, 91, 43, 96),
    (-180, -160, 190, 20)
])
def ShouldCreateSectorTest(minDirection: float, maxDirection: float, expectedDirection: float, expectedWidth: float):
    sector = Sector.FromBoundaries(math.radians(minDirection), math.radians(maxDirection))
    assert math.isclose(sector.Direction, math.radians(expectedDirection), rel_tol=1e-6) and \
           math.isclose(sector.Width, math.radians(expectedWidth), rel_tol=1e-6)