import os
import shutil
import tempfile
import uuid
from datetime import datetime
from shutil import ignore_patterns

version: str
fileContent: str
sourceDirectoryPath: str
targetDirectoryPath: str
baseSourceDirectoryPath: str
baseTargetDirectoryPath: str

baseSourceDirectoryPath = rf"{ os.path.dirname(__file__) }\.."
baseTargetDirectoryPath = os.path.join(tempfile.gettempdir(), f"{ str(uuid.uuid4()) }", f"v{ datetime.now().strftime('%Y-%m-%d') }")

print(f"Copying files to folder { baseTargetDirectoryPath }.")

# sample -> SiteAssessmentSample
sourceDirectoryPath = os.path.join(baseSourceDirectoryPath, "sample", "SiteAssessmentSample")
targetDirectoryPath = os.path.join(baseTargetDirectoryPath, "sample")

shutil.copytree(sourceDirectoryPath, targetDirectoryPath, ignore=ignore_patterns("__pycache__"))

with open(os.path.join(targetDirectoryPath, "data.site-assessment.json"), "r") as fh:
    fileContent = fh.readlines()

fileContent.insert(1, r'    "$schema": ".\\..\\support\\1.0.0.json",' + "\n")

with open(os.path.join(targetDirectoryPath, "data.site-assessment.json"), "w") as fh:
    fh.writelines(fileContent)

# doc -> IEC_61400_12 -> SiteAssessment
sourceDirectoryPath = os.path.join(baseSourceDirectoryPath, "doc", "IEC_61400_12", "SiteAssessment")
targetDirectoryPath = os.path.join(baseTargetDirectoryPath, "doc")

shutil.copytree(sourceDirectoryPath, targetDirectoryPath, ignore=ignore_patterns("__pycache__"))

# src
sourceDirectoryPath = os.path.join(baseSourceDirectoryPath, "src")
targetDirectoryPath = sourceDirectoryPath.replace(baseSourceDirectoryPath, baseTargetDirectoryPath)

os.makedirs(targetDirectoryPath)

shutil.copyfile(os.path.join(sourceDirectoryPath, "Convention.py"), os.path.join(targetDirectoryPath, "Convention.py"))
shutil.copyfile(os.path.join(sourceDirectoryPath, "Converter.py"), os.path.join(targetDirectoryPath, "Converter.py"))
shutil.copyfile(os.path.join(sourceDirectoryPath, "Geometry.py"), os.path.join(targetDirectoryPath, "Geometry.py"))
shutil.copyfile(os.path.join(sourceDirectoryPath, "ModuleSystem.py"), os.path.join(targetDirectoryPath, "ModuleSystem.py"))
shutil.copyfile(os.path.join(sourceDirectoryPath, "Serialization.py"), os.path.join(targetDirectoryPath, "Serialization.py"))

# src -> IEC_61400_12 -> SiteAssessment
sourceDirectoryPath = os.path.join(baseSourceDirectoryPath, "src", "IEC_61400_12", "SiteAssessment")
targetDirectoryPath = sourceDirectoryPath.replace(baseSourceDirectoryPath, baseTargetDirectoryPath)

shutil.copytree(sourceDirectoryPath, targetDirectoryPath, ignore=ignore_patterns("__pycache__"))

# support -> json-schema -> site-assessment
sourceDirectoryPath = os.path.join(baseSourceDirectoryPath, "support", "json-schema", "site-assessment")
targetDirectoryPath = os.path.join(baseTargetDirectoryPath, "support")

os.makedirs(targetDirectoryPath)

shutil.copyfile(os.path.join(sourceDirectoryPath, "1.0.0.json"), os.path.join(targetDirectoryPath, "1.0.0.json"))

# test -> IEC_61400_12 -> SiteAssessment
sourceDirectoryPath = os.path.join(baseSourceDirectoryPath, "test", "IEC_61400_12", "SiteAssessment")
targetDirectoryPath = os.path.join(baseTargetDirectoryPath, "test")

shutil.copytree(sourceDirectoryPath, targetDirectoryPath, ignore=ignore_patterns("__pycache__"))