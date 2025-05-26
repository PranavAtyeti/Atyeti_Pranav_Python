from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class ErrorSummary(Base):
    __tablename__ = 'error_summary'
    id = Column(Integer, primary_key=True)
    file_name = Column(String, nullable=False)
    count = Column(Integer, nullable=False)
