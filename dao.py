from typing import List

from advpymysql.core.annotations import *
from models import *

@Select("select * from user where username=#{username}", True)
def queryUserByUsername(username) -> User:
    pass

@Select("select * from user")
def queryAllUsers() -> List[User]:
    pass
