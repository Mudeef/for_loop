# def resuable(num):
#     for i in range(1,num):
#         print("This is a resuable function 1")
#         print("This is a resuable function 2")
#         print("This is a resuable function 3")
#         print("This is a resuable function 4")
#         print("---------------------------------------------------")
#
# resuable

# def resuable():
#         print("This is a resuable function 1")
#         print("This is a resuable function 2")
#         print("This is a resuable function 3")
#         print("This is a resuable function 4")
#         print("---------------------------------------------------")
#
# num=int(input("enter a number: "))
# for i in range(1, num):
#     resuable()

print("===================================================================================")

print("*******WELCOME TO CALCULATOR*******")
num1=int(input("Client Enter a Number1:  "))
print(num1)

num2=int(input("Client Enter another Number2:  "))
print(num2)

print("These are the operators you can use: ")
print("1. Addition")
print("2. Substraction ")
print("3. Multiplication")
print("4. Division")
print("5. Modulus")
result=0
operator=input("Please choose an option from these(1,2,3,4,5): ")
def add(num1,num2):
    return num1+num2
def sub(num1,num2):
    return num1 - num2
def mul(num1,num2):
    return num1 * num2
def div(num1,num2):
    return num1 // num2
def mod(num1,num2):
    return num1 % num2
if operator=="1":
    result=add(num1,num2)
    print(result)
if operator == "2":
    result = sub(num1, num2)
    print(result)
if operator == "3":
    result = mul(num1, num2)
    print(result)
if operator == "4":
    result = div(num1, num2)
    print(result)
if operator == "5":
    result = mod(num1, num2)
    print(result)