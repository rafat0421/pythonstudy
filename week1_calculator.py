"""
Week 1: Simple Calculator
This program asks the user for two numbers and one arithmetic operation.
It supports addition, subtraction, multiplication, and division.
"""

# Ask for the two numeric inputs and convert the text input to numbers.
first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))

# Ask the user which calculation to perform.
operation = input("Choose operation (+, -, *, /): ").strip()

# Select and perform the requested operation.
if operation == "+":
    result = first_number + second_number
    print(f"Result: {result}")
elif operation == "-":
    result = first_number - second_number
    print(f"Result: {result}")
elif operation == "*":
    result = first_number * second_number
    print(f"Result: {result}")
elif operation == "/":
    # Division by zero is not allowed, so it needs a separate check.
    if second_number == 0:
        print("Error: division by zero is not allowed.")
    else:
        result = first_number / second_number
        print(f"Result: {result}")
else:
    print("Invalid operation. Please choose +, -, *, or /.")
