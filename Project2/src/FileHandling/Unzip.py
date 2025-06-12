import os
import glob
import zipfile

class Unzip:
    def __init__(self, directory_path):
        self.directory_path = directory_path

    def unzip_all(self):
        zip_files = glob.glob(os.path.join(self.directory_path, "*.zip"))
        all_extracted_files = []

        for zip_path in zip_files:
            zip_name = os.path.basename(zip_path)
            extract_to = os.path.join(self.directory_path, os.path.splitext(zip_name)[0])

            try:
                with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                    zip_ref.extractall(extract_to)
                    print(f"Unzipped: {zip_name} to {extract_to}")
            except zipfile.BadZipFile:
                print(f"Skipping invalid zip file: {zip_name}")
                continue

            extracted_files = glob.glob(os.path.join(extract_to, "*"))
            all_extracted_files.extend(extracted_files)

        print("\nExtracted Files:")
        for file in all_extracted_files:
            print(os.path.basename(file))

        return extract_to

