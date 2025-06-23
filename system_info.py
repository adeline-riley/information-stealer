import os
import platform
import socket

def get_system_info():
    info = {
        "OS": platform.system(),
        "OS Version": platform.version(),
        "Architecture": platform.machine(),
        "Hostname": socket.gethostname(),
        "IP Address": socket.gethostbyname(socket.gethostname()),
        "Processor": platform.processor(),
        "CPU Cores": os.cpu_count()
    }

    with open("system_info.txt", "w") as f:
        f.write("=== System Info ===\n")
        for key, value in info.items():
            f.write(f"{key}: {value}\n")

    print("[+] System info collected (light version).")