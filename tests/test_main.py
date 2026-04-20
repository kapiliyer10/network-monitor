from src.main import run_monitor
import os

def test_run_monitor():
    test_file = "test_devices.txt"
    with open(test_file,"w") as f:
        f.write("127.0.0.1\n")

    run_monitor("test_devices.txt")

    assert os.path.exists("logs/ping_log.txt")
    os.remove(test_file)
