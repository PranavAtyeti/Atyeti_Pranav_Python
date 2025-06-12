from src.FileHandling.Log_Reader import LogReader
from src.FileHandling.Log_Analyzer import LogAnalyzer
from src.FileHandling.Log_Saver import LogSaver
from src.FileHandling.Save_Json import JsonSaver

class LogProcessor:
    def __init__(self, directory, session):
        self.reader = LogReader(directory)
        self.analyzer = LogAnalyzer()
        self.saver = LogSaver(session)
        self.json_saver = JsonSaver()

    def execute(self):
        file_data = self.reader.read_logs()

        if not file_data:
            print("No valid log files found.")
            return

        counts, messages = self.analyzer.analyze(file_data)
        self.saver.save(counts)

        for file_name in file_data:
            self.json_saver.save_json_summary(
                log_counts=counts[file_name],
                messages=messages[file_name],
                log_file=file_name
            )
        print("Json file created successfully!")
