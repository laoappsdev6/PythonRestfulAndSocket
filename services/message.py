class Msg:
    httpRun = "HTTPServer is running on port: "
    webRun = "WebSocketServer is running on port: "
    tcpRun = "TCPServer is running on port: "
    onMsg = "Message from client\n"
    rePly = "Reply to client\n"
    client = "Client connection "
    welcome = "Welcome to my application"

    addSuccess = "Add data successfully."
    addFail = "Add data failed!"
    updateSuccess = "Update data successfully."
    updateFail = "Update data failed!"
    deleteSuccess = "Delete data successfully."
    deleteFail = "Delete data failed!"
    listOne = "Data list One"
    listAll = "Data list All"
    listPage = "Data list Page"

    dbConnectFail = "Connect to database error: "
    dbQueryError = "Query error: "
    objNotFound = "Object not found!"
    methodNotFound = "Method not found!"
    dataEmpty = "Data is empty!"
    isEmpty = "{} is emtpy!"
    isNumber = "{} is number only!"
    alreadyExist = "{}: {} already exist!"
    acountWrong = "Wrong username or password!"
    noAuthorize = "You have no authorize"
    true = "true"


class Sts:
    success = 1
    fail = 0
