import json
import cherrypy
import DataStorage

_clientSet = set()

async def Broadcast(message: str):

    for client in _clientSet:
        try:
            await client.send(message)
        except Exception:
            pass

async def AcceptWsConnection(client, path):

    _clientSet.add(client)

    # Python 3.6:
        # print(f"Websockets: Client connected on path '{ path }'.")
        #
        # async for message in client:
        #     del message

    # Python < 3.6
    del path

    print("Websockets: Client connected.")

    while True:
        try:
            message = await client.recv()

            try:
                if message == "Get10Minutes":
                    await client.send(json.dumps(DataStorage.GetHistoricalData(10)))
                elif message == "Get60Minutes":
                    await client.send(json.dumps(DataStorage.GetHistoricalData(60)))
            except Exception:
                pass

        except Exception:
            break

    _clientSet.remove(client)

    print("Websockets: Client disconnected.")

class Controller(object):

    @cherrypy.expose
    def index(self):
        return open('./wwwroot/index.html')