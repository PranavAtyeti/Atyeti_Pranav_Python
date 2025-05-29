from src.DTO.InfoSummary import InfoSummary
from src.DTO.WarningSummary import WarningSummary
from src.DTO.ErrorSummary import ErrorSummary

class LogSaver:
    def __init__(self, session):
        self.session = session

    def save(self, counts):
        for file_name, count in counts.items():
            self.session.add(InfoSummary(file_name=file_name, count=count['INFO']))
            self.session.add(WarningSummary(file_name=file_name, count=count['WARNING']))
            self.session.add(ErrorSummary(file_name=file_name, count=count['ERROR']))
        
        self.session.commit()
