class LogAnalyzer:
    def analyze(self, file_data):
        counts = {}
        messages = {}

        for file_name, lines in file_data.items():
            info = 0
            warning = 0
            error = 0
            info_msgs = []
            warning_msgs = []
            error_msgs = []

            for line in lines:
                line = line.strip()
                if 'INFO' in line:
                    info += 1
                    info_msgs.append(line)
                elif 'WARNING' in line:
                    warning += 1
                    warning_msgs.append(line)
                elif 'ERROR' in line:
                    error += 1
                    error_msgs.append(line)

            counts[file_name] = {
                'INFO': info,
                'WARNING': warning,
                'ERROR': error
            }

            messages[file_name] = {
                'INFO': info_msgs,
                'WARNING': warning_msgs,
                'ERROR': error_msgs
            }

        return counts, messages
