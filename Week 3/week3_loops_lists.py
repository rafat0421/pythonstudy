"""
Week 3 — Loops and Lists
Advanced participant sample submission.
"""

numbers = [3, -1, 0, 8, -4, 15, -7, 0]

positive_count = 0
negative_count = 0
zero_count = 0
total_sum = 0

# Process each number in the list.
for number in numbers:
    # Add the current number to the running total.
    total_sum += number

    # Classify the number and update the correct counter.
    if number > 0:
        positive_count += 1
    elif number < 0:
        negative_count += 1
    else:
        zero_count += 1

# Print the final summary after the loop has finished.
print("Numbers:", numbers)
print("Positive numbers:", positive_count)
print("Negative numbers:", negative_count)
print("Zeros:", zero_count)
print("Sum:", total_sum)
