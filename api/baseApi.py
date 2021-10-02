from api.loginApi import LoginApi
from api.userApi import UserApi
from servers.request import Request
from servers.response import Response
from services.message import Msg, Sts
from services.myJwt import Jwt
from services.object import Object
from services.service import Service


class BaseApi:

    @staticmethod
    def checkObject(obj: Request) -> Response:

        if not Jwt.jwtDecode(obj.token) and obj.object != Object.login: return Service.getRes([], Msg.noAuthorize, Sts.fail)

        if obj.object == Object.users:
            return UserApi.checkMethod(obj)
        elif obj.object == Object.login:
            return LoginApi.checkMethod(obj)
        else:
            return Service.getRes([], Msg.objNotFound, Sts.fail)
