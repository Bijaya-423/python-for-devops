info = {
    "name": "Bijaya kumar jena", #str
    "city": "Bhubaneswar", #str
    "qualification": "B.Tech", #str
    "age": 23, #int
    "salary": 22.5, #float
    "married": False, #bool
    "favorities": ["Reading", "Travelling", "Cooking"] #list
}
# print(f"i live in {info['city']}")
# print(f"i love {info.get('favoriti', "Not found")}")
# info.update({"blood_group": "O+", "hobbies": "Playing cricket"})
# print(info)
# print(dir(info))
for i in info:
    print(f"{i} : {info[i]}")
    print(i)
    

for key, value in info.items():
    print(key, value)


for i in info.keys():
    print(i)

for  i in info.values():
    print(i)
    