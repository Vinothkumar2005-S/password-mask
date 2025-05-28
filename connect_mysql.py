import pymysql
from password_utils import get_decrypted_password
conn = pymysql.connect(
    host = "localhost",
    user = "root",
    password = "2005",
    database = "vk",
    cursorclass = pymysql.cursors.DictCursor
)

try:
    with conn.cursor() as cursor:
        create_query = """
        create table if not exists employees(
        id int primary key,
        name varchar(100)
        department varchar(100)
        
        );
        """
        cursor.execute(create_query)

        insert_query = "INSERT INTO employees (id, name, department) VALUES (%s, %s, %s)"
        values = [( 'John', 'IT'), ( 'Jane', 'Marketing'),("bob","finance")]
        cursor.executemany(insert_query, values)
        conn.commit()


        select_query = "SELECT * FROM employees"
        cursor.execute(insert_query,values)
        result = cursor.fetchall()

        for row in result:
            print(row)
finally:
    conn.close()

