from controllers.loginController import LoginController
from models.loginModel import LoginModel
from servers.request import Request
from servers.response import Response
from services.message import Msg, Sts
from services.method import LoginMethod
from services.service import Service


class LoginApi:

    @staticmethod
    def checkMethod(obj: Request) -> Response:

        if not obj.data: return Service.getRes([], Msg.dataEmpty, Sts.fail)

        loginModel = LoginModel(**obj.data)

        if obj.method == LoginMethod.login:
            validate = loginModel.validateAll()
            if validate != Msg.true: return Service.getRes([], validate, Sts.fail)
            return LoginController.authorize(loginModel)
        else:
            return Service.getRes([], Msg.methodNotFound, Sts.fail)
