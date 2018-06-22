import sys
import os
import threading
import asyncio
import cherrypy
import websockets
import DataAcquisition
import DataStorage

from Web import Controller, AcceptWsConnection

print(sys.version)

host = "0.0.0.0"
websocketPort = 9001
cherryPyPort = 9000

# initialize storage
DataStorage.Initialize()

# initialize data acquisition
DataAcquisition.Initialize()
task = asyncio.ensure_future(DataAcquisition.UpdateData())

# initialize websockets server
task = asyncio.ensure_future(websockets.serve(AcceptWsConnection, host, websocketPort))

# run all tasks in separate thread
wsThread = threading.Thread(target=asyncio.get_event_loop().run_forever)
wsThread.daemon = True
wsThread.start()

# configure CherryPy
config = {
    "global": {
        "engine.autoreload.on" : False,
        "log.screen": False,
        "server.socket_host": host,
        "server.socket_port": cherryPyPort
    },
    "/": {
        "tools.staticdir.root": os.path.abspath(os.getcwd())
    },
    "/static": {
        "tools.staticdir.on": True,
        "tools.staticdir.dir": "./wwwroot/"
    }
}

# run web server
print("Starting web server.")
cherrypy.quickstart(Controller(), "/", config)
