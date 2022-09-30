class User:
    def __init__(self, id, username, password, role, clazz):
        self._id = id
        self._username = username
        self._role = role
        self._clazz = clazz
        self._password = password

    def getId(self):
        return self._id

    def getUsernaem(self):
        return self._username

    def getRole(self):
        return self._role

    def getClass(self):
        return self._clazz

    def getPassword(self):
        return self._password

    def setId(self, id):
        self._id = id

    def setUsername(self, username):
        self._username = username

    def setRole(self, role):
        self._role = role

    def setClass(self, clazz):
        self._clazz = clazz

    def setPassword(self, password):
        self._password = password