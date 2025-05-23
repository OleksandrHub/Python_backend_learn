from colorama import Fore, Back, Style

print(Back.BLUE)
what = input("What do you want to calculate? (add, sub, mul, div): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if what == "add":
    print(num1 + num2)
elif what == "sub":
    print(num1 - num2)
elif what == "mul":
    print(num1 * num2)
elif what == "div":
    if num2 != 0:
        print(num1 / num2)
    else:
        print("Cannot divide by zero!")
else:
    print("Invalid operation!")