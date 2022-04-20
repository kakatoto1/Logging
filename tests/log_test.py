import os

def test_log_file_exit(log):
    """This makes the index page"""
    response = log.get("info.log")

assert os.path.exists(info.log) == True