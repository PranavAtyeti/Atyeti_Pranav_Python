from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class InfoSummary(Base):
    __tablename__ = 'info_summary'
    id = Column(Integer, primary_key=True)
    file_name = Column(String, nullable=False)
    count = Column(Integer, nullable=False)