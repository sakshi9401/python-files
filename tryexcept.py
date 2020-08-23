num1 = input("enter num1")
num2 = input("enter num2")

try:
    print("the sum of these two numbers are",int(num1)+int(num2))
except Exception as e:
    print(e)

print("subtraction of two no. is",int(num1)-int(num2))