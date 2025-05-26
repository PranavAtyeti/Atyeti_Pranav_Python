from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class DBConnection:
    def __init__(self):
        self.engine = create_engine('mysql+mysqlconnector://root:root@localhost/log_analysis')
        self.Session = sessionmaker(bind=self.engine)

    def get_session(self):
        return self.Session()

    def create_tables(self):
        Base.metadata.create_all(self.engine)
