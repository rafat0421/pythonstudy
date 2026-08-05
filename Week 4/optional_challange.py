# Week 4 Optional Independent Challenge
# Completed without ChatGPT or external help

numbers = [12, -5, 0, 7, -3, 18, 0, -9]

positive_numbers = []
negative_numbers = []
zero_count = 0

total_sum = 0
highest_number = numbers[0]
lowest_number = numbers[0]

for number in numbers:
    total_sum += number

    if number > highest_number:
        highest_number = number

    if number < lowest_number:
        lowest_number = number

    if number > 0:
        positive_numbers.append(number)
    elif number < 0:
        negative_numbers.append(number)
    else:
        zero_count += 1

average = total_sum / len(numbers)

print("Numbers:", numbers)
print("Positive values:", positive_numbers)
print("Negative values:", negative_numbers)
print("Zero count:", zero_count)
print("Positive count:", len(positive_numbers))
print("Negative count:", len(negative_numbers))
print("Sum:", total_sum)
print("Average:", average)
print("Highest:", highest_number)
print("Lowest:", lowest_number)
