# sum = 0
# for i in range(1, 11):
#     sum = sum + i

# print(sum)



# sum = 0

# i = 1

# while i <= 100:
#     sum = sum + i
#     i += 1
# print(sum)

# def sum(n):
#     if n == 1:
#         return 1
#     return n + sum(n-1)
# print(sum(100))


def dum(n):
    if n == 1:
        return 1
    return n + dum(n-1)

print(dum(100))