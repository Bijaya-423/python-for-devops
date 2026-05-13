import os

path = "d:/DEVOps/python-for-devops"

files = []

for file in os.listdir(path):
    if os.path.isfile(file):
        size = os.path.getsize(file)
        files.append((file, size))

files.sort(key=lambda x: x[1], reverse=True)
for file in files[:5]:
    print(f"File: {file[0]}, Size: {file[1]} bytes")
    print(file)