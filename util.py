import hashlib

sha256 = hashlib.sha256()

def sha256String(stringIn:str) -> str:
    sha256.update(stringIn.encode('UTF-8'))
    return sha256.hexdigest()

class Response:
    ...