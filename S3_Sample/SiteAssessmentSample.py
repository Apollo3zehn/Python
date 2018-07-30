import json
import logging
import math
import os

from S1_Framework import Serialization
from S1_Framework.IEC_61400_12 import SiteAssessment

filePath: str
logger: logging.Logger

# get console logger
logger = logging.getLogger("SiteAssessmentSample")
logging.basicConfig(level=logging.INFO)

# deserialize configuration data
filePath = os.path.join(os.path.dirname(os.path.realpath(__file__)), r".\..\S2_Test\TestData\data.site-assessment.json")   

with open(filePath) as fileStream:
    data = json.load(fileStream)

configuration = Serialization.Deserialize(data, SiteAssessment.Configuration)
configuration.Initialize()

# analyze configuration
analyzerParameters = SiteAssessment.AnalyzerParameters()
analyzerParameters.MinSectorWidth = math.radians(20)

analyzer = SiteAssessment.Analyzer(configuration, analyzerParameters)

# 1 - print results to logger
printer = SiteAssessment.Printer(analyzer)
printer.Print(logger)

# 2 - write results to CSV file
csvWriter = SiteAssessment.CsvWriter(analyzer)
csvWriter.Write(r"C:\Users\wilvin\Desktop\siteassessment\test.csv") # TODO change path

# 3 - plot results using matplotlib
plotter = SiteAssessment.Plotter(analyzer)
plotter.Plot()