import mysql.connector
 
conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "logs"
)
 
cursor = conn.cursor()
 
 
 
cursor.close()
conn.close()


def parse_log_file(filepath):
    error_count = 0
    warn_count = 0
    info_count = 0
 
    try:
        with open(filepath, 'r') as f:
            for line in f:
                if '[ERROR]' in line:
                    error_count += 1
                elif '[WARN]' in line or '[WARNING]' in line:
                    warn_count += 1
                elif '[INFO]' in line:
                    info_count += 1
    except Exception as e:
        print(f"Failed to read {filepath}: {e}")
 
    return error_count, warn_count, info_count

filepath = r"C:\Users\PranavChothave\OneDrive - Atyeti Inc\Desktop\pair_prog\Proj1\Logs\log1.log"
print(parse_log_file(filepath))