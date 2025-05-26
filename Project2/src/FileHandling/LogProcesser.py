import os
import glob

from src.DTO.ErrorSummary import ErrorSummary
from src.DTO.InfoSummary import InfoSummary
from src.DTO.WarningSummary import WarningSummary



class LogProcessor:
    def __init__(self, directory, session):
        self.directory = directory
        self.session = session
        self.content = None

    def read_log_files(self):
        log_files = glob.glob(os.path.join(self.directory, "*.log"))
        file_data = {}

        for file_path in log_files:
            try:
                with open(file_path, 'r') as file:
                    lines = file.readlines()
                    file_data[os.path.basename(file_path)] = lines
            except IOError as e:
                print(f"Error reading {file_path}: {e}")
        
        return file_data


    def process_logs(self):
        file_data = self.read_log_files()
        counts = {}

        for file_name, lines in file_data.items():


            info_count = 0
            warning_count = 0
            error_count = 0
            for line in lines:
                if 'INFO' in line:
                    info_count += 1
                elif 'WARNING' in line:
                    warning_count += 1
                elif 'ERROR' in line:
                    error_count += 1

            counts[file_name] = {
                'INFO': info_count,
                'WARNING': warning_count,
                'ERROR': error_count
            }

        return counts


    def save_counts(self):
        counts = self.process_logs()

        for file_name, count_dict in counts.items():
            self.session.add(InfoSummary(file_name=file_name, count=count_dict['INFO']))
            self.session.add(WarningSummary(file_name=file_name, count=count_dict['WARNING']))
            self.session.add(ErrorSummary(file_name=file_name, count=count_dict['ERROR']))
        
        self.session.commit()

