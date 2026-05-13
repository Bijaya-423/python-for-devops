# # print cpu usage every 5 times with 2 seconds interval
# import psutil
# from time import sleep


# count = 1

# while count <= 5:
#     cpu = psutil.cpu_percent()
#     print("CPU %: ", cpu)
#     sleep(2)
#     count += 1



# infinite monitoring if cpu in while true
import psutil
from time import sleep

while True:
    cpu = psutil.cpu_percent()
    memory = psutil.virtual_memory().percent

    print("CPU:", cpu, "%")
    print("Memory:", memory, "%")

    print("-----------------------------")
    sleep(2)
    