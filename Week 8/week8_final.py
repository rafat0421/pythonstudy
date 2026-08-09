# Week 8 - Final Withdrawal and Transfer Test
# Completed without ChatGPT or external help

def calculate_average(students):
    total = 0

    for score in students.values():
        total = total + score

    return total / len(students)


def find_highest_score(students):
    highest_student = None
    highest_score = None

    for student, score in students.items():
        if highest_score is None or score > highest_score:
            highest_student = student
            highest_score = score

    return highest_student, highest_score


def find_lowest_score(students):
    lowest_student = None
    lowest_score = None

    for student, score in students.items():
        if lowest_score is None or score < lowest_score:
            lowest_student = student
            lowest_score = score

    return lowest_student, lowest_score


def classify_score(score):
    if score >= 60:
        return "Pass"
    else:
        return "Fail"


students = {
    "Anna": 88,
    "Erik": 62,
    "Sara": 91,
    "Jonas": 54,
    "Maria": 76
}

average_score = calculate_average(students)
highest_student, highest_score = find_highest_score(students)
lowest_student, lowest_score = find_lowest_score(students)

print("Students:", ", ".join(students.keys()))
print()
print("Average score:", round(average_score, 1))
print("Highest score:", highest_student, "-", highest_score)
print("Lowest score:", lowest_student, "-", lowest_score)
print()

for student, score in students.items():
    result = classify_score(score)
    print(student + ":", result)
