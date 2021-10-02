from servers.response import Response


class Service:

    @staticmethod
    def getRes(data: list, message: str, status: int) -> Response:
        response = Response()
        response.status = status
        response.message = message
        response.data = data
        return response
