import asyncio
import json

import websockets

from api.baseApi import BaseApi
from configs.config import MyConfig
from servers.request import Request
from services.message import Msg


async def Handle(websocket, path):
    async for message in websocket:

        # OnRequest
        jsonData = json.loads(message)
        request = Request(**jsonData)
        print(Msg.onMsg, jsonData)

        # Process
        result = BaseApi.checkObject(request)
        result.object = request.object
        result.method = request.method

        # OnResponse
        response = json.dumps(result.__dict__)
        await websocket.send(response)
        print(Msg.rePly, response)


if __name__ == '__main__':
    start_server = websockets.serve(Handle, MyConfig.webHost, MyConfig.webPort)
    print(Msg.webRun, MyConfig.webPort)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
