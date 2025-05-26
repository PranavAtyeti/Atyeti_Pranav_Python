from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class WarningSummary(Base):
    __tablename__ = 'warning_summary'
    id = Column(Integer, primary_key=True)
    file_name = Column(String, nullable=False)
    count = Column(Integer, nullable=False)

