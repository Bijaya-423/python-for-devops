# count and check how many log file or python file present in a folder

import os

path = "d:/DEVOps/python-for-devops/day-01/practice/"

count = 0

for file in os.listdir(path):
    if file.endswith(".log") or file.endswith(".py"):
        count += 1

print(f"Total log and python files are:- {count}")