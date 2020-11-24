# this class defines a user with username, password , and a select query for houses associated with that user.
class User:
    def __init__(self, name, password):
        self.name = name
        self.password = password

    def getPassword(self):
        return self.password

    def getName(self):
        return self.name
