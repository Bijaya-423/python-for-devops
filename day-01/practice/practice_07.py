# each_char = "Devops Engineer"

# for each in each_char:
#     print(each)



ori_list = [1, 2, 3, 4, 5]
reverse_list = []

i = len(ori_list) - 1

while i >= 0:
    reverse_list.append(ori_list[i])
    i -= 1
print(reverse_list)