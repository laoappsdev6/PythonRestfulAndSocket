from services.message import Msg


class LoginModel:
    def __init__(self, username="", password=""):
        self.username = username
        self.password = password

    def validateAll(self) -> str:
        if not self.username:
            return Msg.isEmpty.format("Username")
        if not self.password:
            return Msg.isEmpty.format("Password")
        return "true"
