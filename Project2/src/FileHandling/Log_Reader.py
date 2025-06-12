import os
import glob
import shutil
from .Log_Validator import Log_Validator

class LogReader:
    def __init__(self, directory):
        self.directory = directory
        self.validator = Log_Validator()
    
    def validate_header_footer(self, filepath):
        return self.validator.validate_header_footer(filepath)


    def read_logs(self):
        log_files = glob.glob(os.path.join(self.directory, "*.txt"))
        destination_path = r"C:\Users\PranavChothave\OneDrive - Atyeti Inc\Desktop\pair_prog\Project2\Resources\Archives"

        for f_path in log_files:
            if not self.validate_header_footer(f_path):
                file_name = os.path.basename(f_path)
                print(f"File {file_name} has been moved to archives!")
                shutil.move(f_path, destination_path)
                log_files.remove(f_path)


        file_data = {}

        for file_path in log_files:
            try:
                with open(file_path, 'r') as file:
                    lines = file.readlines()
                    file_data[os.path.basename(file_path)] = lines
            except IOError as e:
                print(f"Error reading {file_path}: {e}")
            
        return file_data
    
    