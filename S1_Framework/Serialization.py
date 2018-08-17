import inspect

from . import Convention

class Dynamic:

    def __init__(self, data):

        for key, value in data.items():

            key = Convention.KebapCaseToPascalCase(key)

            if isinstance(value, dict):
                setattr(self, key, Dynamic(value))
                
            elif isinstance(value, list):
                convertedValue = [Dynamic(element) if isinstance(element, dict) else element for element in value]
                setattr(self, key, convertedValue)

            else:
                setattr(self, key, value)

def ToDynamic(data):
    return Dynamic(data)

def Deserialize(data, cls):
    
    annotations: list = GetInheritedAnnotations(cls)

    if issubclass(cls, list):

        listType = cls.__args__[0]
        instance: list = list()

        for value in data:
            instance.append(Deserialize(value, listType))

        return instance
        
    elif issubclass(cls, dict):

        keyType = cls.__args__[0]
        valueType = cls.__args__[1]

        instance: dict = dict()

        for key, value in data.items():

            key = Convention.KebapCaseToPascalCase(key)

            instance.update(Deserialize(key, keyType), Deserialize(value, valueType))

        return instance
        
    else:

        instance: cls = cls()

        for name, value in data.items():
            
            name = Convention.KebapCaseToPascalCase(name)
            fieldType = annotations.get(name)

            if inspect.isclass(fieldType) and isinstance(value, (dict, tuple, list, set, frozenset)):
                setattr(instance, name, Deserialize(value, fieldType))
            else:
                setattr(instance, name, value)

        if hasattr(instance, "OnDeserialized"):
            instance.OnDeserialized()

        return instance

def GetAnnotations(cls):
    return cls.__annotations__ if hasattr(cls, '__annotations__') else dict()

def GetInheritedAnnotations(cls):
    
    baseTypeSet = inspect.getmro(cls)
    
    return dict([annotation for baseType in baseTypeSet for annotation in GetAnnotations(baseType).items()])