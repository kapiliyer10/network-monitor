from src.utils.ping import ping_device
from datetime import datetime
import threading
import os

def check_device(ip,log_file,lock):
    status = ping_device(ip)
    time = datetime.now()
    print("CI test")
    with lock:

        if status:

            log_file.write(f"{time} INFO {ip} is UP \n")
            print(f"{ip} is UP")

        else:
            log_file.write(f"{time} ERROR {ip} is DOWN \n")
            print(f"{ip} is DOWN")


def run_monitor(devices_file = "devices.txt"):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    devices_path = os.path.join(BASE_DIR,devices_file)
    log_dir = os.path.join(BASE_DIR,"logs")

    os.makedirs(log_dir,exist_ok=True)
    log_path = os.path.join(log_dir,"ping_log.txt")
    lock = threading.Lock()
    threads = []

    with open(log_path,"w") as log_file:
        with open(devices_path,"r") as dev_file:
            for line in dev_file:
                ip = line.strip()
                thread = threading.Thread(target = check_device, args = (ip,log_file,lock))
                threads.append(thread)
                thread.start()

        for thread in threads:
            thread.join()

if __name__ == "__main__":
    run_monitor()
