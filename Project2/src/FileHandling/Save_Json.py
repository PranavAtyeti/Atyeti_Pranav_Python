import os
import json
import time

class JsonSaver:
    def __init__(self, output_root=r"C:\Users\PranavChothave\OneDrive - Atyeti Inc\Desktop\pair_prog\Project2\Resources\Output"):
        self.output_root = output_root
        os.makedirs(self.output_root, exist_ok=True)

    def save_json_summary(self, log_counts, messages, log_file):
        timestamp = time.strftime("%Y%m%d%H%M%S")

        folder_path = os.path.join(self.output_root, timestamp)
        os.makedirs(folder_path, exist_ok=True)

        json_filename = f"{timestamp}_{log_file}.json"
        output_path = os.path.join(folder_path, json_filename)

        data = {
            "file_name": log_file,
            "date_of_creation": timestamp,
            "log_levels": {
                "info": {
                    "messages": messages.get("INFO", []),
                    "count": log_counts.get("INFO", 0)
                },
                "error": {
                    "messages": messages.get("ERROR", []),
                    "count": log_counts.get("ERROR", 0)
                },
                "warning": {
                    "messages": messages.get("WARNING", []),
                    "count": log_counts.get("WARNING", 0)
                }
            }
        }

        with open(output_path, 'w') as f:
            json.dump(data, f, indent=2)
