Get the Enviornment from user and print it

env = input("Enter the env:- ")
print("The enviornment is:-", env)

#----------------------------------------------------------------

a = int(input("Enter the value of a: "))
#Typecasting - converting one datatype to another datatype
print(type(a))
b = int(input("Enter the value of b: "))
print(type(b))

print("mul: ", a*b )
print("add: ", a+b )
print("sub: ", a-b )
print("div: ", a/b )

#--------------------------------------------------------------

a = input("Enter:-")
print("The value of a is:-", a)
print(type(a))

b = input("Enter:-")
print("The value of b is:-", b)
print(type(b))

print("The addition of a and b is:-", a+b)
print("The multiplication of a and b is:-", a*b)

#-------------------------------------------------------------

env = input("Enter the enviornment:-")
print("The enviornment is:-", env)

if env == "prod":
    print("Don't deploy on friday.")

elif env == "staging":
    print("Deploy on friday")

else:
    print("You can do anything.")

#--------------------------------------------------------------

env = input("Enter the enviornment:-")
print("The enviornment is:-", env)

if env == "prod":
    print("Don't deploy on friday.")
elif env == "staging":
    print("Take backup and test well.")
else:
    print("Safe to deploy any day.")