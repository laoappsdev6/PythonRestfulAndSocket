import jwt


class Jwt:

    @staticmethod
    def jwtEncode(data: str) -> str:
        myJwt = jwt.encode(data, "secret", algorithm="HS256")
        return myJwt

    @staticmethod
    def jwtDecode(data: str) -> bool:
        if data:
            try:
                jwt.decode(data, "secret", algorithms=["HS256"])
                return True
            except (jwt.InvalidTokenError, jwt.DecodeError) as err:
                print(err)
                return False
        else:
            return False
