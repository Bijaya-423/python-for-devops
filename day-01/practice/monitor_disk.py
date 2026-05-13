import psutil
import time

while True:
    disk = psutil.disk_usage('/').percent
    print("Disk Usage:", disk, '%')

    if disk > 80:
        print("DISK ALERT: Disk usage is crossed 80%.")
        break
    time.sleep(2)