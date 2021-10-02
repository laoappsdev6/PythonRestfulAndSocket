from services.message import Msg


class UserModel:
    def __init__(self, id="", name="", username="", password="", phoneNumber="", remark="", page="", limit=""):
        self.id = id
        self.name = name
        self.username = username
        self.password = password
        self.phoneNumber = phoneNumber
        self.remark = remark
        self.page = page
        self.limit = limit

    def validateAll(self, insert=False, update=False, delete=False) -> str:
        if update or delete:
            if type(self.id) != int:
                return Msg.isNumber.format("Id")
        if insert or update:
            if not self.name:
                return Msg.isEmpty.format("Name")
            if not self.username:
                return Msg.isEmpty.format("Username")
            if not self.password:
                return Msg.isEmpty.format("Password")
            if not self.phoneNumber:
                return Msg.isEmpty.format("PhoneNumber")
        return Msg.true
