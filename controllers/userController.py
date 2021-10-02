from controllers.databaseController import DatabaseController, count
from models.userModel import UserModel
from servers.response import Response
from services.message import Msg, Sts
from services.service import Service


class UserController:

    @staticmethod
    def add(data: UserModel) -> Response:
        sqlCheck = "select count(*) as num from users where username='{}'".format(data.username)
        numCount = count(sqlCheck)
        print(numCount)
        if numCount > 0:
            return Service.getRes([],  Msg.alreadyExist.format("Username", data.username), Sts.fail)
        else:
            sql = "insert into users (name,username,password,phonenumber,remark) values(%s,%s,%s,%s,%s)"
            values = (data.name, data.username, data.password, data.phoneNumber, data.remark)
            return DatabaseController.insert(sql, values)

    @staticmethod
    def update(data: UserModel) -> Response:
        sqlCheck = "select count(*) as num from users where username='{0}' and id!='{1}'".format(data.username, data.id)
        numCount = count(sqlCheck)
        print(numCount)
        if numCount > 0:
            return Service.getRes([], Msg.alreadyExist.format("Username", data.username), Sts.fail)
        else:
            sql = "update users set name=%s,username=%s,password=%s,phonenumber=%s,remark=%s where id=%s"
            values = (data.name, data.username, data.password, data.phoneNumber, data.remark, data.id)
            return DatabaseController.update(sql, values)

    @staticmethod
    def delete(data: UserModel) -> Response:
        sql = "delete from users where id={}".format(data.id)
        return DatabaseController.delete(sql)

    @staticmethod
    def listOne(data: UserModel) -> Response:
        sql = "select * from users where id={}".format(data.id)
        return DatabaseController.selectOne(sql)

    @staticmethod
    def listAll() -> Response:
        sql = "select * from users order by id desc"
        return DatabaseController.selectAll(sql)

    @staticmethod
    def listPage(data: UserModel) -> Response:
        page = data.page
        limit = data.limit
        offset = (page - 1) * limit
        sqlCount = "select count(*) as num from users"
        sqlPage = "select * from users order by id desc limit {0} offset {1}".format(limit, offset)
        return DatabaseController.selectPage(sqlCount, sqlPage)
