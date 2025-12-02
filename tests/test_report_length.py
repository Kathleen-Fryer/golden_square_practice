from lib.report_length import * 

def test_report_length_four():
    result = report_length("four")
    assert result == "This string was 4 characters long"

def test_report_length_feathers_mcgraw():
    result = report_length("Feathers Mcgraw")
    assert result == "This string was 15 characters long"

def test_report_length_empty():
    result = report_length("")
    assert result == "This string was empty"