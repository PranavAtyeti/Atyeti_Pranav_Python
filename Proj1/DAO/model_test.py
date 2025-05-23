from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine("mysql+mysqlconnector://root:root@localhost/org")
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class Organization(Base):
    __tablename__ = 'organization'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    city = Column(String(100), nullable=False)

class Error_logs(Bas)

Base.metadata.create_all(engine)

new_org = Organization(name="abc", city="pune")
session.add(new_org)
session.commit()

new_org2 = Organization(name="xyz", city ="mumbai")
session.add(new_org2)
session.commit()

print(f"Inserted: {new_org.name}, {new_org.city}")
