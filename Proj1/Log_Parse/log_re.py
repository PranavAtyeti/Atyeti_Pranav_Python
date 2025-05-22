import re

def parse_log(line):
    pattern = r'^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\s+(INFO|ERROR|WARNING)\s+\[([^\]]+)\]\s+-\s+(.+)$'
    match = re.match(pattern, line)
    if match:
        return match.groups()
    return None