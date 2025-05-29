class LogAnalyzer:
    def analyze(self, file_data):
        counts = {}

        for file_name, lines in file_data.items():
            info = 0
            warning = 0
            error = 0
            for line in lines:
                if 'INFO' in line:
                    info += 1
                elif 'WARNING' in line:
                    warning += 1
                elif 'ERROR' in line:
                    error += 1


            counts[file_name] = {
                'INFO': info,
                'WARNING': warning,
                'ERROR': error
            }

        return counts
