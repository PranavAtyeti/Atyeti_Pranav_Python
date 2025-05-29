from src.DAO.Connection import DBConnection
from src.FileHandling.Log_Processor import LogProcessor

from src.FileHandling.Unzip import Unzip

def main():
    db = DBConnection()
    db.create_tables()

    session = db.get_session()

    log_directory = r"C:\Users\PranavChothave\OneDrive - Atyeti Inc\Desktop\pair_prog\Project2\Resources"
    processor = LogProcessor(directory=log_directory, session=session)
    processor.execute()

    print("working on Unzipping")
    unzip = Unzip(log_directory)
    extracted_files = unzip.unzip_all()
    processor2 = LogProcessor(directory=extracted_files, session=session)
    processor2.execute()


if __name__ == "__main__":
    main()
