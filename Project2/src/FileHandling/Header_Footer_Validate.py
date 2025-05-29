import os

class Header_Footer_Validate:
    def __init__(self,filepath):
        self.filepath = filepath

    def validate_header_footer(self):
        file_name = os.path.basename(self.filepath)
        flag1, flag2 = 0,0

        with open(self.filepath, 'r') as file:
            lines = [line.strip() for line in file.readlines()]

        header = lines[0]

        header_filename, header_date = header.split(",", 1)
        if (header_filename == file_name) and (header_date.isdigit() and len(header_date) == 8):
            print(f"Valid Header in {file_name}.")
            flag1 = 1

        footer = lines[-1]
        expected_line_count = len(lines) - 2

        if (footer.isdigit()) and (int(footer) == expected_line_count):
            print(f"Valid Footer in {file_name}.")
            flag2 = 1
        if(flag1 and flag2):
            print("valid header footer")

# filepath1 = r"C:\Users\PranavChothave\OneDrive - Atyeti Inc\Desktop\pair_prog\Project2\Resources\log4.txt"
# obj1 = Header_Footer_Validate(filepath1)
# obj1.validate_header_footer()
