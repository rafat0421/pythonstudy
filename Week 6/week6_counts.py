# Week 6 - Strings and Dictionaries

def clean_text(text):
    punctuation_marks = [".", ",", "!", "?", ";", ":"]
    text = text.lower()

    for mark in punctuation_marks:
        text = text.replace(mark, "")

    return text


def count_words(text):
    word_counts = {}
    words = text.split()

    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1

    return word_counts


sentence = input("Enter a sentence: ")

cleaned_sentence = clean_text(sentence)
word_counts = count_words(cleaned_sentence)

print("Word counts:")

for word in sorted(word_counts):
    print(word + ":", word_counts[word])

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
