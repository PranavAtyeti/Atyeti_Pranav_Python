import os
import glob
from .log_re import parse_log
from .db_connect import get_connection, setup_log_tables, insert_log

def process_store_logs(directory):
    conn = get_connection()
    if not conn:
        return
    
    cursor = conn.cursor()
    setup_log_tables(conn)

    log_files = glob.glob(os.path.join(directory, "*.log"))

    for file_path in log_files:
        file_name = os.path.basename(file_path)
        try:
            with open(file_path,'r') as file:
                for line in file:
                    parsed = parse_log(line)
                    print(f"Parsing line: {line.strip()}")
                    print(f"Parsed result: {parsed}")
                    if parsed:
                        timestamp, level, service, message = parsed
                        table = {
                            "INFO":"info_log",
                            "WARNING":"warning_log",
                            "ERROR":"error_log"
                        }.get(level)

                        if table:
                            insert_log(cursor,table,timestamp,file_name,service,message)

        except Exception as e:
            print(f"Failed to process {file_path}:{e}")

    cursor.close()
    conn.close()
    print("Processing complete")