import math
from typing import List, Tuple

import numpy
import pytest
from numpy import ndarray

from S1_Framework.IEC_61400_12.SiteAssessment.BaseTypes import \
    TerrainProperties

@pytest.mark.parametrize("data", [([1, 2], [1, 2], [0, 0], 0), ([1, 2], [0, 0], [0, 1], 100), ([0, 0], [1, 2], [0, 1], 100), ([1, 2], [1, 2], [0, 1], 1 / math.sqrt(2) * 100), ([0, 1, 1], [1, 1, 0], [0, 1, 0], 141.4214)])
def ShouldCalculatePlaneSlopeTest(data: List[Tuple]):
    
    x: ndarray
    y: ndarray
    heightSet: ndarray
    referenceHeight: float
    expectedPlaneSlope: float
    terrainProperties: TerrainProperties

    x = numpy.array(data[0])
    y = numpy.array(data[1])
    heightSet = numpy.array(data[2])
    expectedPlaneSlope = data[3]

    referenceHeight = 10
    terrainProperties = TerrainProperties(x, y, heightSet, referenceHeight)

    from S1_Framework.IEC_61400_12.SiteAssessment import PlotTerrainSlopePlane
    PlotTerrainSlopePlane(terrainProperties, [0, 1, 2, 3], [0, 1, 2, 3])

    assert math.isclose(terrainProperties.PlaneSlope, expectedPlaneSlope, abs_tol=1e-3)

@pytest.mark.parametrize("data", [([1, 2], [1, 2], [0, 0], 0), ([1, 2], [0, 0], [0, 1], 50), ([0, 0], [1, 2], [0, 1], 50), ([1, 2], [1, 2], [0, 1], 35.3554), ([0, 1, 1], [1, 1, 0], [0, 1, 0], 1 / math.sqrt(2) * 100)])
def ShouldCalculateMaxPointSlopeTest(data: List[Tuple]):
    
    x: ndarray
    y: ndarray
    heightSet: ndarray
    referenceHeight: float
    expectedMaxPointSlope: float
    terrainProperties: TerrainProperties

    x = numpy.array(data[0])
    y = numpy.array(data[1])
    heightSet = numpy.array(data[2])
    expectedMaxPointSlope = data[3]

    referenceHeight = 0
    terrainProperties = TerrainProperties(x, y, heightSet, referenceHeight)
    
    assert math.isclose(terrainProperties.MaxPointSlope, expectedMaxPointSlope, abs_tol=1e-3)

@pytest.mark.parametrize("data", [([1, 2], [1, 2], [0, 0], 0), ([1, 2], [0, 0], [0, 1], 0), ([0, 0], [1, 2], [0, 1], 0), ([1, 2], [1, 2], [0, 1], 0), ([0, 1, 1], [1, 1, 0], [0, 1, 0], 0)])
def ShouldCalculateMaxTerrainVariationTest(data: List[Tuple]):
    
    x: ndarray
    y: ndarray
    heightSet: ndarray
    referenceHeight: float
    expectedMaxPointSlope: float
    terrainProperties: TerrainProperties

    x = numpy.array(data[0])
    y = numpy.array(data[1])
    heightSet = numpy.array(data[2])
    expectedMaxPointSlope = data[3]

    referenceHeight = 0
    terrainProperties = TerrainProperties(x, y, heightSet, referenceHeight)
    
    assert math.isclose(terrainProperties.MaxTerrainVariation, expectedMaxPointSlope, abs_tol=1e-3) 