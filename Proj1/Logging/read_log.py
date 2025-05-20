import glob
import os

def read_log_files(directory):

    log_files = glob.glob(os.path.join(directory, "*.log"))

    for file_path in log_files:
        try:
            with open(file_path, 'r') as file:
                print(f"Contents of {file_path}:")
                print(file.read())
        except IOError as e:
            print(f"Error reading {file_path}: {e}")

directory_path = r"C:\Users\PranavChothave\OneDrive - Atyeti Inc\Desktop\pair_prog\Proj1\Logging"
read_log_files(directory_path)