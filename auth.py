import dao
from models import User

def login(username, password):
    user = dao.queryUserByUsername(username)
    if user is None:
        return