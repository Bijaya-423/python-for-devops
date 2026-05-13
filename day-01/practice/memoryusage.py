import psutil
from time import sleep


count = 0

while count < 12:
    memory = psutil.virtual_memory().percent
    print("Memory usage:", memory, "%")
    sleep(5)
    count += 1
    