import time
import platform
from datetime import datetime

def get_interval(arch):
    if 'x86' in arch:
        return 10
    elif 'x86_64' in arch:
        return 7
    elif 'arm' in arch:
        return 3
    else:
        return 5

def log_time():
    arch = platform.machine().lower()
    interval = get_interval(arch)
    
    while True:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        timestamp = datetime.now().timestamp()
        
        if 'x86' in arch:
            print(f"Текущее время: {current_time}")
        else:
            print(f"Текущее время: {current_time}")

        time.sleep(interval)

if __name__ == "__main__":
    log_time()
