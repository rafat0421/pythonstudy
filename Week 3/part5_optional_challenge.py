"""
Week 3 — Optional Challenge
Advanced participant sample submission.
"""

numbers = []

print("Enter numbers one at a time.")
print("Type 'stop' when you are finished.")

while True:
    user_input = input("Enter a number or stop: ").strip()

    if user_input.lower() == "stop":
        break

    try:
        number = float(user_input)
        numbers.append(number)
    except ValueError:
        print("Invalid input. Please enter a number or type stop.")

positive_numbers = []
negative_numbers = []
zero_values = []

total_sum = 0
highest_number = None
lowest_number = None

for number in numbers:
    total_sum += number

    if highest_number is None or number > highest_number:
        highest_number = number

    if lowest_number is None or number < lowest_number:
        lowest_number = number

    if number > 0:
        positive_numbers.append(number)
    elif number < 0:
        negative_numbers.append(number)
    else:
        zero_values.append(number)

print()
print("Numbers:", numbers)
print("Positive numbers:", positive_numbers)
print("Negative numbers:", negative_numbers)
print("Zeros:", zero_values)
print("Positive count:", len(positive_numbers))
print("Negative count:", len(negative_numbers))
print("Zero count:", len(zero_values))
print("Sum:", total_sum)

if len(numbers) > 0:
    average = total_sum / len(numbers)
    print("Average:", average)
    print("Highest number:", highest_number)
    print("Lowest number:", lowest_number)
else:
    print("No numbers were entered.")
