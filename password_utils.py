from cryptography.fernet import Fernet

class Fakestr(str):
    def __str__(self):
        return "******"
    def __repr__(self):
        return "******"

def load_key():
    return open("secret.key", "rb").read()

def encrypt_password(password):
    key = load_key()
    f = Fernet(key)
    return f.encrypt(password.encode())

def decrypt_password(encrypted_password):
    key = load_key()
    f = Fernet(key)
    decrypted = f.decrypt(encrypted_password).decode()
    return Fakestr(decrypted)


def get_decrypted_password():
    encrypt_password = b'gAAAAABoNaDsLm-F_o1YGZJ1a3_8suMhzJH2lG_abQSPR40UwzlGoLT8pErecanqva6L6WcmMmk9rcBqaO_xPTlnbtXxxWtuXQ=='
    return decrypt_password(encrypt_password)