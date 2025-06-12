import pytest
from src.FileHandling.Log_Analyzer import LogAnalyzer

@pytest.fixture
def analyzer():
    return LogAnalyzer()

def test_single_log_file_with_all_levels(analyzer):
    file_data = {
        "test_log.txt": [
            "INFO Application started",
            "WARNING Low disk space",
            "ERROR Unable to connect",
            "INFO Processing data"
        ]
    }

    counts, messages = analyzer.analyze(file_data)

    assert counts["test_log.txt"]["INFO"] == 2
    assert counts["test_log.txt"]["WARNING"] == 1
    assert counts["test_log.txt"]["ERROR"] == 1

    assert "INFO Application started" in messages["test_log.txt"]["INFO"]
    assert "WARNING Low disk space" in messages["test_log.txt"]["WARNING"]
    assert "ERROR Unable to connect" in messages["test_log.txt"]["ERROR"]

def test_empty_file(analyzer):
    file_data = {
        "empty_log.txt": []
    }

    counts, messages = analyzer.analyze(file_data)

    assert counts["empty_log.txt"]["INFO"] == 0
    assert counts["empty_log.txt"]["WARNING"] == 0
    assert counts["empty_log.txt"]["ERROR"] == 0

    assert messages["empty_log.txt"]["INFO"] == []
    assert messages["empty_log.txt"]["WARNING"] == []
    assert messages["empty_log.txt"]["ERROR"] == []

def test_file_with_unknown_lines(analyzer):
    file_data = {
        "mixed_log.txt": [
            "DEBUG Not tracked",
            "INFO Valid line",
            "Something random here"
        ]
    }

    counts, messages = analyzer.analyze(file_data)

    assert counts["mixed_log.txt"]["INFO"] == 1
    assert counts["mixed_log.txt"]["WARNING"] == 0
    assert counts["mixed_log.txt"]["ERROR"] == 0

    assert messages["mixed_log.txt"]["INFO"] == ["INFO Valid line"]
    assert messages["mixed_log.txt"]["WARNING"] == []
    assert messages["mixed_log.txt"]["ERROR"] == []
