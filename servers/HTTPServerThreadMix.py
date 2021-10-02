import threading
from http.server import BaseHTTPRequestHandler, HTTPServer
from socketserver import ThreadingMixIn

from api.baseApi import BaseApi
from configs.config import MyConfig
from servers.request import Request
from services.message import Msg
import json

class Handler(BaseHTTPRequestHandler):

    def do_POST(self):

        # OnRequest
        headerContent = int(self.headers.get('Content-Length'))
        bodyData = self.rfile.read(headerContent)
        jsonData = json.loads(bodyData)
        request = Request(**jsonData)
        print(Msg.onMsg, jsonData)

        # Process
        result = BaseApi.checkObject(request)
        result.object = request.object
        result.method = request.method

        # OnResponse
        response = json.dumps(result.__dict__)
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(bytes(response, "utf8"))
        print(Msg.rePly, response)


class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    pass


if __name__ == '__main__':
    server = ThreadedHTTPServer((MyConfig.webHost, MyConfig.httpPort), Handler)
    print(Msg.httpRun, MyConfig.httpPort)
    server.serve_forever()
