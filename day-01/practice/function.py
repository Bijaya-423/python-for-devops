#function = write the business logic once and use it many times

# SCRIPT = SET OF INSTRUCTIONS TO PERFORM A SPECIFIC TASK

# input the 2 numbers and and print the sum
def sum_of_num(num1, num2):

    # num1 = int(input("Enter the first number:- "))
    # num2 = int(input("Enter the second number:- "))

    sum = num1 + num2
    print(sum)

env = input("Enter the env:- ")
print(f'The user input env is {env}')

if env == "prod":
    sum_of_num(num1=int(input("num1: ")), num2=int(input("num2: ")))


def take_backup():
    print("Backup script started......")

day = input("Enter the day:- ")
if day == "monday":
    take_backup()