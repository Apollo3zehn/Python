import sys
import os
import json
import logging

from S2_Internal import PowerPerformance

# https://code.visualstudio.com/docs/languages/json#_mapping-in-the-user-settings

def GeneralTest():

    logger = logging.getLogger("PowerPerformanceTests")
    logging.basicConfig(level=logging.INFO)

    filePath = os.path.join(os.path.dirname(os.path.realpath(__file__)), r".\TestData\data.site-assessment.json")

    with open(filePath) as fileStream:
        data = json.load(fileStream)
        
    PowerPerformance.SiteAssessment.Calculate(data, logger)

    raise Exception()