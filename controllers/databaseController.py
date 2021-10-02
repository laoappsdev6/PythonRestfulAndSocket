import mysql.connector
from configs.config import MyConfig
from servers.response import Response
from services.message import Msg, Sts
from services.service import Service


class DatabaseController:

    @staticmethod
    def connection():
        try:
            return mysql.connector.connect(
                host=MyConfig.dbHost,
                user=MyConfig.dbUser,
                password=MyConfig.dbPass,
                database=MyConfig.dbName
            )
        except mysql.connector.Error as err:
            print(Msg.dbConnectFail, err)
            return False

    @staticmethod
    def insert(sql: str, values: tuple) -> Response:
        result = query(sql, values)
        if result:
            return Service.getRes([], Msg.addSuccess, Sts.success)
        else:
            return Service.getRes([], Msg.addFail, Sts.fail)

    @staticmethod
    def update(sql: str, values: tuple) -> Response:
        result = query(sql, values)
        if result:
            return Service.getRes([], Msg.updateSuccess, Sts.success)
        else:
            return Service.getRes([], Msg.updateFail, Sts.fail)

    @staticmethod
    def delete(sql: str) -> Response:
        result = query(sql, 0)
        if result:
            return Service.getRes([], Msg.deleteSuccess, Sts.success)
        else:
            return Service.getRes([], Msg.deleteFail, Sts.fail)

    @staticmethod
    def selectOne(sql: str) -> Response:
        result = select(sql)
        return Service.getRes(result, Msg.listOne, Sts.success)

    @staticmethod
    def selectAll(sql: str) -> Response:
        result = select(sql)
        return Service.getRes(result, Msg.listAll, Sts.success)

    @staticmethod
    def selectPage(sqlCount: str, sqlPage: str) -> Response:
        number = count(sqlCount)
        dataList = []
        if number > 0:
            rsPage = select(sqlPage)
            obj = {"count": number, "rows": rsPage}
            dataList.append(obj)
        else:
            obj = {"count": number, "rows": []}
            dataList.append(obj)
        return Service.getRes(dataList, Sts.success, Sts.success)


def count(sql: str) -> int:
    db = DatabaseController()
    conn = db.connection()
    if conn is False: return 0
    if not sql: return 0

    try:
        cursor = conn.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        return int(result[0][0])
    except mysql.connector.Error as err:
        print(Msg.dbQueryError, err)
        return 0


def select(sql: str):
    db = DatabaseController()
    conn = db.connection()
    if conn is False: return False
    if not sql: return False

    try:
        cursor = conn.cursor()
        cursor.execute(sql)
        rowHeaders = [x[0] for x in cursor.description]
        myList = cursor.fetchall()
        jsonData = []
        for result in myList:
            jsonData.append(dict(zip(rowHeaders, result)))
        cursor.close()
        conn.close()
        return jsonData
    except mysql.connector.Error as err:
        print(Msg.dbQueryError, err)
        return False


def query(sql: str, values: tuple) -> bool:
    db = DatabaseController()
    conn = db.connection()
    if conn is False: return False
    if not sql: return False

    try:
        cursor = conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()
        return True
    except mysql.connector.Error as err:
        print(Msg.dbQueryError, err)
        return False
