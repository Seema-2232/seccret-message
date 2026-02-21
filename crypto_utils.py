import base64
from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def encrypt_message(message, key):
    f = Fernet(key)
    encrypted = f.encrypt(message.encode())
    return encrypted.decode()

def decrypt_message(token, key):
    f = Fernet(key)
    decrypted = f.decrypt(token.encode())
    return decrypted.decode()