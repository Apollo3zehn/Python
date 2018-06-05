from . import ExampleSubPackage

def HighLevelPrint():
    print("ExampleModule.py executed")
    ExampleSubPackage.ExampleSubModule.LowLevelPrint()
    return