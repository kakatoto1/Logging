import os.path

def log_test_exist():
    # get root directory of project
    root = os.path.dirname(os.path.abspath(__file__))
    # set the name of the apps log folder to logs
    logdir = os.path.join(root, 'logs')

    log_file = os.path.join(logdir, 'info.log')

    assert os.path.exists(log_file) == True