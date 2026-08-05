# Week 5 Optional Challenge
# Expert participant sample

def has_minimum_length(password):
    return len(password) >= 8


def has_digit(password):
    return any(character.isdigit() for character in password)


def has_uppercase(password):
    return any(character.isupper() for character in password)


def has_lowercase(password):
    return any(character.islower() for character in password)


def has_special_character(password):
    special_characters = "!@#$%^&*()-_=+[]{};:,.<>?/"

    for character in password:
        if character in special_characters:
            return True

    return False


def validate_password(password):
    failed_rules = []

    if not has_minimum_length(password):
        failed_rules.append("at least 8 characters")

    if not has_digit(password):
        failed_rules.append("at least one digit")

    if not has_uppercase(password):
        failed_rules.append("at least one uppercase letter")

    if not has_lowercase(password):
        failed_rules.append("at least one lowercase letter")

    if not has_special_character(password):
        failed_rules.append("at least one special character")

    return failed_rules


def run_tests():
    print("Testing helper functions:")
    print("has_minimum_length('Python123'):", has_minimum_length("Python123"))
    print("has_digit('Python123'):", has_digit("Python123"))
    print("has_uppercase('python123'):", has_uppercase("python123"))
    print("has_lowercase('PYTHON123'):", has_lowercase("PYTHON123"))
    print("has_special_character('Python123!'):", has_special_character("Python123!"))
    print()


def main():
    run_tests()

    while True:
        password = input("Enter password or type quit: ")

        if password.lower() == "quit":
            print("Program stopped.")
            break

        failed_rules = validate_password(password)

        if len(failed_rules) == 0:
            print("Password is valid.")
        else:
            print("Password is invalid.")
            print("Missing rules:")
            for rule in failed_rules:
                print("-", rule)

        print()


main()
