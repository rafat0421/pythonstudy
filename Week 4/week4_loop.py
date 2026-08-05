# Week 4 - Withdrawal Checkpoint 1
# Expert participant sample
# Completed without ChatGPT or external help

numbers = [12, -5, 0, 7, -3, 18, 0, -9]

positive_count = 0
negative_count = 0
zero_count = 0
total_sum = 0

for number in numbers:
    total_sum += number

    if number > 0:
        positive_count += 1
    elif number < 0:
        negative_count += 1
    else:
        zero_count += 1

print("Numbers:", numbers)
print("Positive:", positive_count)
print("Negative:", negative_count)
print("Zero:", zero_count)
print("Sum:", total_sum)
