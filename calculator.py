# this python program is for a simple calculator
"""
create a function
create a variable for an input function for the operators
using (if, elif and else)control statement,
make the variable name == to the variable name of each operator
create two input statement using (int) data type
to convert from strings to integer
print the result using (str) to convert it back to a string
then call the created function
"""


def cal():
    operatior = (input("enter operator:"))
    if operatior == "add":
        num1 = int(input("enter your first number:"))
        num2 = int(input("enter your second number:"))
        print(str(num1 + num2))

    elif operatior == "sub":
        num1 = int(input("enter your first number:"))
        num2 = int(input("enter your second number:"))
        print(str(num1 - num2))

    elif operatior == "divide":
        num1 = int(input("enter your first number:"))
        num2 = int(input("enter your second number:"))
        print(str(num1 / num2))

    elif operatior == "multiply":
        num1 = int(input("enter your first number:"))
        num2 = int(input("enter your second number:"))
        print(str(num1 * num2))

    elif operatior == "modulus":
        num1 = int(input("enter your first number:"))
        num2 = int(input("enter your second number:"))
        print(str(num1 % num2))

    elif operatior == "power":
        num1 = int(input("enter your first number:"))
        num2 = int(input("enter your second number:"))
        print(str(num1 ** num2))

    else:
        print("The operator is invalid")


cal()
