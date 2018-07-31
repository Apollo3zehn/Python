import json
import logging
import math
import os
import tempfile
import uuid

from S1_Framework import Serialization
from S1_Framework.IEC_61400_12 import SiteAssessment

configFilePath: str
tempFilePath: str
logger: logging.Logger

# deserialize configuration data
configFilePath = os.path.join(os.path.dirname(os.path.realpath(__file__)), "data.site-assessment.json")   

with open(configFilePath) as fileStream:
    data = json.load(fileStream)

configuration = Serialization.Deserialize(data, SiteAssessment.Configuration)
configuration.Initialize()

# analyze configuration
analyzerParameters = SiteAssessment.AnalyzerParameters()
analyzerParameters.MinSectorWidth = math.radians(20)

analyzer = SiteAssessment.Analyzer(configuration, analyzerParameters)

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
plotter.Plot()
