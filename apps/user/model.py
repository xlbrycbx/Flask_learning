class User:
    def __init__(self,username,password,phone=None):
        self.username = username
        self.password = password
        self.phone = phone

    def str(self):
        return self.username
