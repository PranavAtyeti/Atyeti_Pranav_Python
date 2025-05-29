from src.FileHandling.Log_Reader import LogReader
from src.FileHandling.Log_Analyzer import LogAnalyzer
from src.FileHandling.Log_Saver import LogSaver

class LogProcessor:
    def __init__(self, directory, session):
        self.reader = LogReader(directory)
        self.analyzer = LogAnalyzer()
        self.saver = LogSaver(session)

    def execute(self):
        file_data = self.reader.read_logs()
        counts = self.analyzer.analyze(file_data)
        self.saver.save(counts)
