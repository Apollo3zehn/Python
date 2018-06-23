from . import Convention

class Dynamic:

    def __init__(self, data):

        for key, value in data.items():

            key = Convention.KebapCaseToPascalCase(key)

            if isinstance(value, dict):
                setattr(self, key, Dynamic(value))

            if isinstance(value, list):
                convertedValue = [Dynamic(element) if isinstance(element, dict) else element for element in value]
                setattr(self, key, convertedValue)

            else:
                setattr(self, key, value)

def ToDynamic(data):
    return Dynamic(data)