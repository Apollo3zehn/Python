import os
import shutil
import tempfile
import uuid
from datetime import datetime

version: str
fileContent: str
sourceDirectoryPath: str
targetDirectoryPath: str
baseSourceDirectoryPath: str
baseTargetDirectoryPath: str

baseSourceDirectoryPath = rf"{ os.path.dirname(__file__) }\.."
baseTargetDirectoryPath = os.path.join(tempfile.gettempdir(), f"{ str(uuid.uuid4()) }", f"v{ datetime.now().strftime('%Y-%m-%d') }")

print(f"Copying files to folder { baseTargetDirectoryPath }.")

# S0_Files -> json-schema
sourceDirectoryPath = os.path.join(baseSourceDirectoryPath, "S0_Files", "json-schema")
targetDirectoryPath = sourceDirectoryPath.replace(baseSourceDirectoryPath, baseTargetDirectoryPath)

os.makedirs(targetDirectoryPath)

shutil.copyfile(os.path.join(sourceDirectoryPath, "site-assessment.json"), os.path.join(targetDirectoryPath, "site-assessment.json"))

# S1_Framework
sourceDirectoryPath = os.path.join(baseSourceDirectoryPath, "S1_Framework")
targetDirectoryPath = sourceDirectoryPath.replace(baseSourceDirectoryPath, baseTargetDirectoryPath)

os.makedirs(targetDirectoryPath)

shutil.copyfile(os.path.join(sourceDirectoryPath, "Convention.py"), os.path.join(targetDirectoryPath, "Convention.py"))
shutil.copyfile(os.path.join(sourceDirectoryPath, "Converter.py"), os.path.join(targetDirectoryPath, "Converter.py"))
shutil.copyfile(os.path.join(sourceDirectoryPath, "Geometry.py"), os.path.join(targetDirectoryPath, "Geometry.py"))
shutil.copyfile(os.path.join(sourceDirectoryPath, "Serialization.py"), os.path.join(targetDirectoryPath, "Serialization.py"))

# S1_Framework -> IEC_61400_12 -> SiteAssessment
sourceDirectoryPath = os.path.join(baseSourceDirectoryPath, "S1_Framework", "IEC_61400_12", "SiteAssessment")
targetDirectoryPath = sourceDirectoryPath.replace(baseSourceDirectoryPath, baseTargetDirectoryPath)

shutil.copytree(sourceDirectoryPath, targetDirectoryPath)

# S3_Sample -> SiteAssessmentSample
sourceDirectoryPath = os.path.join(baseSourceDirectoryPath, "S3_Sample", "SiteAssessmentSample")
targetDirectoryPath = baseTargetDirectoryPath

shutil.copyfile(os.path.join(sourceDirectoryPath, "data.site-assessment.json"), os.path.join(targetDirectoryPath, "data.site-assessment.json"))
shutil.copyfile(os.path.join(sourceDirectoryPath, "SiteAssessmentSample.py"), os.path.join(targetDirectoryPath, "SiteAssessmentSample.py"))

with open(os.path.join(targetDirectoryPath, "data.site-assessment.json"), "r") as fh:
    fileContent = fh.readlines()

fileContent.insert(1, '    "$schema": ".\\\\S0_Files\\\\json-schema\\\\site-assessment.json",\n')

with open(os.path.join(targetDirectoryPath, "data.site-assessment.json"), "w") as fh:
    fh.writelines(fileContent)