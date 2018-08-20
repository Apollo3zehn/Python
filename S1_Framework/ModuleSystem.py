from typing import List

import pkg_resources
from pkg_resources import DistributionNotFound, VersionConflict


def CheckRequirements(dependencySet: List[str]):

    message: str

    message = ""

    for dependency in dependencySet:

        try: 
            pkg_resources.require(dependency)

        except DistributionNotFound as ex:
            message += ex.report() + "\n"

        except VersionConflict as ex:
            message += ex.report() + "\n"

    if any(message):
        raise Exception(f"\n\nThere are missing packages or conflicting package versions:\n\n{ message }")
