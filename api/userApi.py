from controllers.userController import UserController
from models.userModel import UserModel
from servers.request import Request
from servers.response import Response
from services.message import Msg, Sts
from services.method import UserMethod
from services.service import Service


class UserApi:

    @staticmethod
    def checkMethod(obj: Request) -> Response:

        if not obj.data and obj.method != UserMethod.listAll: return Service.getRes([], Msg.dataEmpty, Sts.fail)

        userModel = UserModel(**obj.data)

        if obj.method == UserMethod.add:
            validate = userModel.validateAll(True)
            if validate != Msg.true: return Service.getRes([], validate, Sts.fail)
            return UserController.add(userModel)

        elif obj.method == UserMethod.update:
            validate = userModel.validateAll(False, True)
            if validate != Msg.true: return Service.getRes([], validate, Sts.fail)
            return UserController.update(userModel)

        elif obj.method == UserMethod.delete:
            validate = userModel.validateAll(False, False, True)
            if validate != Msg.true: return Service.getRes([], validate, Sts.fail)
            return UserController.delete(userModel)

        elif obj.method == UserMethod.listOne:
            return UserController.listOne(userModel)

        elif obj.method == UserMethod.listAll:
            return UserController.listAll()

        elif obj.method == UserMethod.listPage:
            return UserController.listPage(userModel)

        else:
            return Service.getRes([], Msg.methodNotFound, Sts.fail)
