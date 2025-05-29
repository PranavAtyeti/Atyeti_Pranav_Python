import os
import glob

class LogReader:
    def __init__(self, directory):
        self.directory = directory
        
    def validate_header_footer(self,filepath):
        file_name = os.path.basename(filepath)
        flag1, flag2 = 0,0

        with open(filepath, 'r') as file:
            lines = [line.strip() for line in file.readlines()]

        header = lines[0]

        header_filename, header_date = header.split(",", 1)
        if (header_filename == file_name) and (header_date.isdigit() and len(header_date) == 8):
            flag1 = 1
        else:
            print(f"Invalid Header in {file_name}.")

        footer = lines[-1]
        expected_line_count = len(lines) - 2

        if (footer.isdigit()) and (int(footer) == expected_line_count):
            flag2 = 1
        else:
            print(f"Invalid Footer in {file_name}.")


        if(flag1 and flag2):
            print(f"{file_name} is valid")
            return True
 


    def read_logs(self):
        log_files = glob.glob(os.path.join(self.directory, "*.txt"))

        for f_path in log_files:
            if not self.validate_header_footer(f_path):
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
    
    