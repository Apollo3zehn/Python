import math
from typing import List, Tuple

import numpy
import pytest
from numpy import ndarray

from S1_Framework.IEC_61400_12.SiteAssessment.BaseTypes import \
    TerrainProperties


@pytest.mark.parametrize("data", [([1, 2], [1, 2], [1, 2], 9)])
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
    expectedPlaneSlope = math.radians(data[3])

    referenceHeight = 10
    terrainProperties = TerrainProperties(x, y, heightSet, referenceHeight)

    assert terrainProperties.PlaneSlope == expectedPlaneSlope
