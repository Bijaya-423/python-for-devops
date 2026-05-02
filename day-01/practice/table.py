# num = int(input("Enter a number:-"))

# for i in range(1, 11):
#     print(f"{num} x {i} = {num * i}")

# name = input("Enter your name:-")

# print(f"Hello dosto, {name} kaise ho?")



# suraj = "chand"
# while suraj == "chand":
#     name = input("Enter your name:-")
#     print(f"Hello dosto, {name} kaise ho?")
#     break

#real world
choice = input("Enter your choice (press q to quit): ")

while choice != "q":
    num = int(input("Enter a number you want the table for:-"))

    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")
