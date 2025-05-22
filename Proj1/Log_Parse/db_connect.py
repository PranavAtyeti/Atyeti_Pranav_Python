import mysql.connector
from mysql.connector import Error

def get_connection():
    try:
        conn = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "root",
            database = "logs"
        )
        return conn
    except IOError as e:
        print(f"Database connection failed: {e}")
        return None    

def setup_log_tables(conn):
    cursor = conn.cursor()
    for table in ['info_log','warning_log','error_log']:
        cursor.execute(f'''
        create table if not exists {table}(
        id int auto_increment primary key,
        log_file varchar(255),
        err_count int(25)
        )
    ''')
    conn.commit()


def insert_log(cursor, table, file_name):
    query = f'''
    insert into {table} (log_file,err_count)
    values (%s,%s)
    '''
    cursor.execute(query,(file_name, err_count))