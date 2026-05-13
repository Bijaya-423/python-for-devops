# count = 0

# with open("app.log", "r") as file:
#     for line in file:
#         if line.strip(): #check if the line is not empty
#             count += 1
# print(f"Total number of lines in the log file are:- {count}")



import os

path_file = "app.log"

if os.path.exists(path_file):
    with open(path_file, "r") as file:
        count = 0
        for line in file:
            if line.strip():
                count += 1
        print(f"Total number of lines in the log file are:- {count}")
else:
    print(f"File -{ {path_file} }- does not exist")