"""
Part 1 — Week 2: Grade Classifier and Login Validator

This program:
1. asks the user for a score between 0 and 100,
2. classifies the score into A, B, C, D, or F,
3. asks for username and password,
4. checks whether both login values are correct.
"""

print("Week 2: Grade Classifier and Login Validator")

# Ask for the score.
# input() returns text, so float() converts it to a number.
score = float(input("Enter score between 0 and 100: "))

# First check whether the score is outside the valid range.
# Then classify the valid score from highest grade to lowest grade.
if score < 0 or score > 100:
    print("Invalid score. Please enter a score between 0 and 100.")
elif score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")

print()

# Stored correct login details.
correct_username = "student"
correct_password = "python123"

# Ask the user for login information.
username = input("Enter username: ")
password = input("Enter password: ")

# Both username and password must be correct, so the condition uses and.
if username == correct_username and password == correct_password:
    print("Login successful")
else:
    print("Login failed. Username or password is incorrect.")
