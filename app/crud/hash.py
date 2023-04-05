import base64
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)

def hash_token(token: str) -> str:
    info_to_hash = token
    message_bytes = info_to_hash.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')
    return base64_message
    
def decode_token(token: str) -> str:
    info_to_hash = token
    message_bytes = info_to_hash.encode('ascii')
    decode_to_text = base64.b64decode(message_bytes)
    decoded_text = decode_to_text.decode('ascii')
    return decoded_text
    


# Encode a string



