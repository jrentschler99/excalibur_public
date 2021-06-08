





class Jasper:
    jasper_server_addr = ""
    jasper_username = ""
    jasper_password = ""

    # initialize class with URL of the server, username and password
    # server URL should NOT have a trailing slash
    def __init__(self, server_uri=None, username=None, password=None):
        self.jasper_server_addr = server_uri
        self.jasper_username = username
        self.jasper_password = password

