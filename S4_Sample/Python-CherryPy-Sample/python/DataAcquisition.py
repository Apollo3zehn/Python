import datetime
import random
import json
import asyncio
import statistics
import Web
import DataStorage

def Initialize():
    print("Data acquisition module initialized.")

async def UpdateData():

    windSpeed = [None] * 10
    windDirection = [None] * 10
    ambientTemperature = [None] * 10
    ambientPressure = [None] * 10

    while True:

        dateTime = datetime.datetime.now()

        for x in range(0, 10):

            # collect data
            windSpeed[x] = GetWindSpeed()
            windDirection[x] = GetWindDirection()
            ambientTemperature[x] = GetAmbientTemperature()
            ambientPressure[x] = GetAmbientPressure()

            message = {}
            message["type"] = "stream"
            message["data"] = [windSpeed[x], windDirection[x], ambientTemperature[x], ambientPressure[x]]

            await Web.Broadcast(json.dumps(message))

            # sleep
            await asyncio.sleep(0.5)

        # store and broadcast data
        DataStorage.Insert(
            dateTime,
            statistics.mean(windSpeed),
            statistics.mean(windDirection),
            statistics.mean(ambientTemperature),
            statistics.mean(ambientPressure))

def GetWindSpeed():
    return round(random.uniform(4, 15), 2)

def GetWindDirection():
    return round(random.uniform(240, 270), 2)

def GetAmbientTemperature():
    return round(random.uniform(15, 17), 2)

def GetAmbientPressure():
    return round(random.uniform(950, 1050), 2)