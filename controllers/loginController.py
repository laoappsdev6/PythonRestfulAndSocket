from controllers.databaseController import select
from models.loginModel import LoginModel
from servers.response import Response
from services.message import Sts, Msg
from services.myJwt import Jwt
from services.service import Service


class LoginController:

    @staticmethod
    def authorize(data: LoginModel) -> Response:
        sql = "select id,name,username,phonenumber,remark from users where username='{}' and password='{}'".format(
            data.username, data.password)
        result = select(sql)
        if result:
            rows = result[0]
            dataJwt = Jwt.jwtEncode(rows)
            obj = {"jwt": dataJwt, "rows": rows}
            return Service.getRes([obj], Msg.welcome, Sts.success)
        else:
            return Service.getRes([], Msg.acountWrong, Sts.success)
