import os

class Log_Validator:
    def validate_header_footer(self,filepath):
            file_name = os.path.basename(filepath)
            flag1, flag2 = 0,0

            with open(filepath, 'r') as file:
                lines = [line.strip() for line in file.readlines()]

            header = lines[0]

            header_filename, header_date = header.split(",", 1)
            if (header_filename == file_name) and (header_date.isdigit() and len(header_date) == 8):
                flag1 = 1
            else:
                print(f"Invalid Header in {file_name}.")

            footer = lines[-1]
            expected_line_count = len(lines) - 2

            if (footer.isdigit()) and (int(footer) == expected_line_count):
                flag2 = 1
            else:
                print(f"Invalid Footer in {file_name}.")


            if(flag1 and flag2):
                print(f"{file_name} is valid")
                return True