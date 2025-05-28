import pymysql
from password_utils import get_decrypted_password

def connect_mysql():
    conn = pymysql.connect(
        host = "localhost",
        user = "root",
        password= get_decrypted_password(),
        database = "vk"
    )

    print("connected to Mysql successfully")
    print(get_decrypted_password())
    conn.close()

if __name__ == "__main__":
    connect_mysql()


