"""
Week 1 Optional Challenge
Features included:
- Functions for each calculation
- Repeated calculations until the user exits
- try/except for invalid number input
- Calculation history
"""

def add(number_one, number_two):
    return number_one + number_two


def subtract(number_one, number_two):
    return number_one - number_two


def multiply(number_one, number_two):
    return number_one * number_two


def divide(number_one, number_two):
    if number_two == 0:
        return None
    return number_one / number_two


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


history = []

while True:
    first_number = get_number("Enter the first number: ")
    second_number = get_number("Enter the second number: ")
    operation = input("Choose operation (+, -, *, /): ").strip()

    if operation == "+":
        result = add(first_number, second_number)
    elif operation == "-":
        result = subtract(first_number, second_number)
    elif operation == "*":
        result = multiply(first_number, second_number)
    elif operation == "/":
        result = divide(first_number, second_number)
        if result is None:
            print("Error: division by zero is not allowed.")
            continue
    else:
        print("Invalid operation. Please choose +, -, *, or /.")
        continue

    calculation = f"{first_number} {operation} {second_number} = {result}"
    history.append(calculation)
    print(f"Result: {calculation}")

    continue_choice = input("Do you want another calculation? (yes/no): ").strip().lower()
    if continue_choice != "yes":
        break

print("\nCalculation history:")
if history:
    for calculation in history:
        print(calculation)
else:
    print("No completed calculations were saved.")
