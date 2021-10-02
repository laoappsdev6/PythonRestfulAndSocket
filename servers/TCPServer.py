import json
import socketserver

from api.baseApi import BaseApi
from configs.config import MyConfig
from servers.request import Request
from services.message import Msg


class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            # OnRequest
            self.data = self.request.recv(1024).strip()
            jsonData = json.loads(self.data)
            request = Request(**jsonData)
            print(Msg.onMsg, jsonData)

            # Process
            result = BaseApi.checkObject(request)
            result.object = request.object
            result.method = request.method

            # OnResponse
            response = json.dumps(result.__dict__)
            self.request.sendall(bytes(response, "utf8"))
            print(Msg.rePly, response)

if __name__ == '__main__':
    with socketserver.TCPServer((MyConfig.webHost, MyConfig.tcpPort), MyTCPHandler) as server:
        print(Msg.tcpRun, MyConfig.tcpPort)
        server.serve_forever()
