import os
import json
import logging

from S1_Framework import Serialization
from S1_Framework.IEC_61400_12 import SiteAssessment

# https://code.visualstudio.com/docs/languages/json#_mapping-in-the-user-settings
# https://www.deine-berge.de/Rechner/Koordinaten/Dezimal/51.525904,8.607483

def GeneralTest():

    logger = logging.getLogger("PowerPerformanceTests")
    logging.basicConfig(level=logging.INFO)

    filePath = os.path.join(os.path.dirname(os.path.realpath(__file__)), r".\TestData\data.site-assessment.json")   

    with open(filePath) as fileStream:
        data = json.load(fileStream)
    
    configuration = Serialization.Deserialize(data, SiteAssessment.Configuration)
    configuration = SiteAssessment.Calculate(configuration, logger)

    raise Exception()