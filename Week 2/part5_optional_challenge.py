"""
Part 5 — Optional Challenge

This program extends the Week 2 task by:
1. using try/except for non-numeric score input,
2. rejecting scores below 0 and above 100,
3. using a classify_grade(score) function,
4. allowing three login attempts,
5. adding a role check.
"""


def classify_grade(score):
    """Return a grade based on the score."""
    if score < 0 or score > 100:
        return "Invalid"
    elif score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


print("Week 2 Optional Challenge")

try:
    score = float(input("Enter score between 0 and 100: "))
    grade = classify_grade(score)

    if grade == "Invalid":
        print("Invalid score. Please enter a value between 0 and 100.")
    else:
        print("Grade:", grade)

except ValueError:
    print("Invalid input. Please enter a numeric score.")

print()

correct_username = "student"
correct_password = "python123"
correct_role = "student"

max_attempts = 3

for attempt in range(1, max_attempts + 1):
    username = input("Enter username: ")
    password = input("Enter password: ")
    role = input("Enter role (admin/student): ").strip().lower()

    if (
        username == correct_username
        and password == correct_password
        and role == correct_role
    ):
        print("Login successful")
        break

    remaining_attempts = max_attempts - attempt

    if remaining_attempts > 0:
        print("Login failed. Attempts remaining:", remaining_attempts)
    else:
        print("Login failed. Program locked.")
