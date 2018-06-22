import datetime
import peewee as pw

_database = pw.SqliteDatabase("meteo.db")

class Meteo(pw.Model):

    class Meta:
        database = _database

    date_time = pw.DateTimeField()
    wind_speed = pw.DoubleField()
    wind_direction = pw.DoubleField()
    ambient_temperature = pw.DoubleField()
    ambient_pressure = pw.DoubleField()

def Initialize():

    _database.connect()

    if not _database.table_exists("meteo"):
        _database.create_tables([Meteo])

    print("Data storage module initialized.")

def Insert(date_time, wind_speed, wind_direction, ambient_temperature, ambient_pressure):

    dataset = Meteo.create(date_time=date_time, wind_speed=wind_speed, wind_direction=wind_direction, ambient_temperature=ambient_temperature, ambient_pressure=ambient_pressure)
    dataset.save()

    _database.commit()

def GetHistoricalData(minutes):

    dateTimeBegin = datetime.datetime.now() - datetime.timedelta(minutes=minutes)

    entries = list(Meteo.select().where(Meteo.date_time >= dateTimeBegin))

    message = {}
    message["type"] = str(minutes) + " minutes"
    message["date_time"] = [i.date_time.isoformat() for i in entries]
    message["data"] = [
        [i.wind_speed for i in entries],
        [i.wind_direction for i in entries],
        [i.ambient_temperature for i in entries],
        [i.ambient_pressure for i in entries]
    ]

    return message