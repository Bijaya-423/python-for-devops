
import psutil 

def check_cpu():
    current_cpu = psutil.cpu_percent(interval=1)
    current_memory = psutil.virtual_memory().percent
    current_disk = psutil.disk_usage('/').percent

    print(f"Current CPU usage: {current_cpu}%")
    print(f"Current Memory Usage: {current_memory}%")
    print(f"Current Disk Usage: {current_disk}%")

    cpu_threshold = int(input("\nEnter CPU threshold:-"))

    if current_cpu > cpu_threshold:
        print("CPU Alert Email Sent...")
    else:
        print("CPU in safe state...")
    
    memory_threshold = int(input("\nEnter Memory threshold:-"))
    if current_memory > memory_threshold:
        print("Memory Alert Email Sent...")
    else:
        print("Memory in safe state...")
    
    disk_threshold = int(input("\nEnter Disk threshold:-"))
    if current_disk > disk_threshold:
        print("Disk Alert Email Sent...")
    else:
        print("Disk in safe State...")

check_cpu()