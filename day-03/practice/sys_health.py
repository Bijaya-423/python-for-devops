import psutil


def check_system_health():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    print(f"CPU Usage: {cpu}%")
    print(f"Memory Usage: {memory}%")
    print(f"Disk Usage: {disk}%")
check_system_health()