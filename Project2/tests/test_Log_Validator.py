import os
import tempfile
import pytest
from src.FileHandling.Log_Validator import Log_Validator  

@pytest.fixture
def validator():
    return Log_Validator()

def create_temp_file(lines):
    fd, path = tempfile.mkstemp(text=True)
    with os.fdopen(fd, 'w') as tmp:
        tmp.write('\n'.join(lines))
    return path

def test_valid_log_file(validator):
    file_name = "valid_log.txt"
    lines = [
        f"{file_name},20250101",
        "INFO Start",
        "WARNING Something",
        "ERROR Crash",
        "3"
    ]
    path = create_temp_file(lines)
    os.rename(path, path.replace(os.path.basename(path), file_name))  
    new_path = os.path.join(os.path.dirname(path), file_name)

    try:
        assert validator.validate_header_footer(new_path) is True
    finally:
        os.remove(new_path)

def test_invalid_header(validator):
    lines = [
        "WRONGFILE.txt,20250101",  
        "INFO",
        "1"
    ]
    path = create_temp_file(lines)

    try:
        assert validator.validate_header_footer(path) is not True
    finally:
        os.remove(path)

def test_invalid_footer(validator):
    file_name = "invalid_footer.txt"
    lines = [
        f"{file_name},20250101",
        "INFO",
        "0"  
    ]
    path = create_temp_file(lines)
    os.rename(path, path.replace(os.path.basename(path), file_name))
    new_path = os.path.join(os.path.dirname(path), file_name)

    try:
        assert validator.validate_header_footer(new_path) is not True
    finally:
        os.remove(new_path)
