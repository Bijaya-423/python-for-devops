# print("Print numbers from 1 to 50 using for loop.")
# from time import sleep

# for i in range(1, 51):

#     sleep(1)
#     if i % 2 == 0:
#         print(i)
#         if i == 10:
#             continue
#     # print(i)


# print("Print only even numbers from 1 to 10")

# nums = int(input("Enter the numbers:- "))

# for i in range(nums):
#     if i % 2 == 0:
#         print(i)


# for i in range(0, 101, 2):
#     print(i)


# def count(count):
#     while count != 101:
#         if count % 2 == 0:
#             print(count)
#         count += 1
    
# count(0)


# print("print 0 to 100 without using for loop")

# count = 0
# while count <= 100:
#     print(count)
#     count += 1

count = 0
while True:
    # print(count)
    if count == 100:
        break
    if count % 3 == 0:
        print(count)
    count+=1