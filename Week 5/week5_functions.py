# Week 5 - Functions and Decomposition
# Expert participant sample

def has_minimum_length(password):
    return len(password) >= 8


def has_digit(password):
    return any(character.isdigit() for character in password)


def has_uppercase(password):
    return any(character.isupper() for character in password)


def has_lowercase(password):
    return any(character.islower() for character in password)


def validate_password(password):
    failed_rules = []

    if not has_minimum_length(password):
        failed_rules.append("Password must contain at least 8 characters.")

    if not has_digit(password):
        failed_rules.append("Password must contain at least one digit.")

    if not has_uppercase(password):
        failed_rules.append("Password must contain at least one uppercase letter.")

    if not has_lowercase(password):
        failed_rules.append("Password must contain at least one lowercase letter.")

    return failed_rules


password = input("Enter password: ")

failed_rules = validate_password(password)

if len(failed_rules) == 0:
    print("Password is valid.")
else:
    print("Password is invalid.")
    print("Failed rules:")
    for rule in failed_rules:
        print("-", rule)
