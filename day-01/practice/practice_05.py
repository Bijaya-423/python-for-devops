import os

path = "d:/DEVOps/python-for-devops/"

for file in os.listdir(path=path):
    if file.endswith(".py"):
        print(file)

for file in os.listdir(path):
    print(file)

for file in os.listdir(path=path):
    if os.path.isfile(os.path.join(path, file)):
        print(file)


for file in os.listdir(path=path):
    if file.endswith(".md"): #and os.path.isfile(os.path.join(path, file)):
        print(file)


for folder, subfolder, files in os.walk(path):
    print("Folder: - ",folder)
    print("Sub-folder:-", subfolder)
    print("Files:-", files)

    for file in files:
        print(file)
    for sub in subfolder:
        print(sub)
