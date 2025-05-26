from src.DAO.Connection import DBConnection
from src.FileHandling.LogProcesser import LogProcessor

def main():
    db = DBConnection()
    db.create_tables()

    session = db.get_session()
    processor = LogProcessor(directory=r"C:\Users\PranavChothave\OneDrive - Atyeti Inc\Desktop\pair_prog\Project2\Resources", session=session)
    processor.save_counts()

if __name__ == "__main__":
    main()
