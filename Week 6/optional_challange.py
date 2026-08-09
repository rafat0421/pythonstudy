# Week 6 Optional Challenge
# Expert participant sample

def clean_text(text):
    punctuation_marks = [".", ",", "!", "?", ";", ":"]
    text = text.lower()

    for mark in punctuation_marks:
        text = text.replace(mark, "")

    return text


def count_words(text):
    counts = {}

    for word in text.split():
        counts[word] = counts.get(word, 0) + 1

    return counts


def print_word_counts(counts):
    print("Word counts:")

    for word in sorted(counts):
        print(word + ":", counts[word])


def find_student_grade(student_grades, student_name):
    return student_grades.get(student_name)


sentence = input("Enter a sentence: ")

cleaned_sentence = clean_text(sentence)
word_counts = count_words(cleaned_sentence)

print_word_counts(word_counts)

student_grades = {
    "Sara": "A",
    "Ali": "B",
    "Maria": "A",
    "John": "C"
}

print()
print("Student grades:")
for student, grade in student_grades.items():
    print(student + ":", grade)

print()
student_name = input("Enter a student name to search: ")
grade = find_student_grade(student_grades, student_name)

if grade is None:
    print("Student not found.")
else:
    print(student_name + "'s grade:", grade)
