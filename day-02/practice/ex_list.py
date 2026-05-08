# list is collection of similiar or disimilar types of datatypes belongs to builtins module to get the manual of list we can use help(list)

# list = [1, 1.2, 1+2j, "python", [1, 2, 3], (1, 2, 3), {1: "one", 2: "two"}, {1, 2, 3}, True, None]



# a = 100
# a = 200
# print(type(a))
# print(a)

a = [100, 200, 300, True, 4.3, None]
print(type(a))
a.append(400)
print(a)

clouds = list()
print(type(clouds))

clouds.append("AWS")
clouds.append("GCP")
clouds.append("Oracle")
clouds.append("IBM")
clouds.append("Alibaba")
clouds.append("Salesforce")
clouds.append("utho")
clouds.append("oracle")
print(clouds)
clouds.append("Azure")
print(clouds)

print(len(clouds))

print("world leader for cloud service provided is :", clouds[0])
print("indian cloud service provider is :", clouds[6])
print("indian cloud service provider is :", clouds[-3])

print(dir(clouds))
# print(clouds.count.__doc__)
# print(clouds.reverse.__doc__)
# print(clouds.append.__doc__)
# print(clouds.extend.__doc__)
# print(clouds.insert.__doc__)
# print(clouds.pop.__doc__)
print(clouds.sort.__doc__)
# print(clouds.copy.__doc__)
# print(clouds.clear.__doc__)