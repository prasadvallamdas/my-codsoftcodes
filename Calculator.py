import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def square_root(x):
    return math.sqrt(x)

def power(x, y):
    return x ** y

def calculate(operation, x, y):
    if operation == '+':
        return add(x, y)
    elif operation == '-':
        return subtract(x, y)
    elif operation == '*':
        return multiply(x, y)
    elif operation == '/':
        return divide(x, y)
    elif operation == '√':
        return square_root(x)
    elif operation == '^':
        return power(x, y)

print("Select operation:")
print("+: Add")
print("-: Subtract")
print("*: Multiply")
print("/: Divide")
print("√: Square Root")
print("^: Power")

operation = input("Enter operation: ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

result = calculate(operation, num1, num2)

print("Result: ", result)