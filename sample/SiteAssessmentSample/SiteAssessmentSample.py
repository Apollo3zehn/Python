import json
import logging
import os
import tempfile
import uuid

import matplotlib.pyplot as plt
import numpy
from numpy import ndarray
from PIL import Image

from src import Serialization
from src.IEC_61400_12 import SiteAssessment

image: Image
heightMap: ndarray
configFilePath: str
heightMapFilePath: str
tempFilePath: str
logger: logging.Logger

# deserialize configuration data
configFilePath = os.path.join(os.path.dirname(os.path.realpath(__file__)), "data.site-assessment.json")   

with open(configFilePath) as fileStream:
    data = json.load(fileStream)

configuration = Serialization.Deserialize(data, SiteAssessment.Configuration)
configuration.Initialize()

# load height map data
heightMapFilePath = os.path.join(os.path.dirname(os.path.realpath(__file__)), "height_map.png")   
image = numpy.array(Image.open(heightMapFilePath))
heightMap = image[..., 0]
heightMap = heightMap[:-1, :-1] * 2 - 40

# analyze configuration
analyzer = SiteAssessment.Analyzer(configuration, heightMapWtg=heightMap, heightMapWme=heightMap)

# 1 - print results to logger
logger = logging.getLogger("SiteAssessmentSample")
logging.basicConfig(level=logging.INFO)

printer = SiteAssessment.Printer(analyzer)
printer.Print(logger)

# 2 - write results to CSV file
tempFilePath = os.path.join(tempfile.gettempdir(), f"{ str(uuid.uuid4()) }.csv")

csvWriter = SiteAssessment.CsvWriter(analyzer)
csvWriter.Write(tempFilePath)

print(f"Results have been written to file { tempFilePath }.")

# 3 - plot results using matplotlib
plotter = SiteAssessment.Plotter(analyzer)

plotResult = plotter.PreparePlot()
plotResult.Wtg.Axis.set_title("I hijacked this title.")

plt.show()
