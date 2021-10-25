print("enter num 1")
num1= input()
print("enter num 2")
num2 = input()
try:
    print("the sum is ", int(num1) + int(num2))
# if we get error in try , except code will be executed
except Exception as e :
    print(e)
print("this line is very important")
