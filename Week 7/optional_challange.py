# Week 7 Optional Challenge
# Expert participant sample

def read_file(file_name):
    with open(file_name, "r") as file:
        return file.read()


def clean_word(word):
    punctuation_marks = ".,!?;:"
    word = word.lower()

    for mark in punctuation_marks:
        word = word.replace(mark, "")

    return word


def analyze_text(text, keyword):
    lines = text.splitlines()
    raw_words = text.split()
    cleaned_words = []

    for word in raw_words:
        cleaned_word = clean_word(word)

        if cleaned_word != "":
            cleaned_words.append(cleaned_word)

    keyword = keyword.lower()
    word_frequencies = {}

    for word in cleaned_words:
        word_frequencies[word] = word_frequencies.get(word, 0) + 1

    keyword_count = word_frequencies.get(keyword, 0)

    most_common_word = None
    highest_count = 0

    for word, count in word_frequencies.items():
        if count > highest_count:
            most_common_word = word
            highest_count = count

    return {
        "line_count": len(lines),
        "word_count": len(cleaned_words),
        "keyword": keyword,
        "keyword_count": keyword_count,
        "word_frequencies": word_frequencies,
        "most_common_word": most_common_word,
        "highest_count": highest_count
    }


def create_summary(file_name, analysis):
    summary = ""
    summary += "File analyzed: " + file_name + "\n"
    summary += "Lines: " + str(analysis["line_count"]) + "\n"
    summary += "Words: " + str(analysis["word_count"]) + "\n"
    summary += "Keyword '" + analysis["keyword"] + "': " + str(analysis["keyword_count"]) + "\n"

    if analysis["most_common_word"] is not None:
        summary += "Most common word: " + analysis["most_common_word"] + " (" + str(analysis["highest_count"]) + " times)\n"

    summary += "\nAll word frequencies:\n"

    for word in sorted(analysis["word_frequencies"]):
        summary += word + ": " + str(analysis["word_frequencies"][word]) + "\n"

    return summary


def write_summary(file_name, summary):
    with open(file_name, "w") as file:
        file.write(summary)


input_file = input("Enter input file name: ")
keyword = input("Enter keyword to search for: ")
output_file = "output.txt"

try:
    text = read_file(input_file)
    analysis = analyze_text(text, keyword)
    summary = create_summary(input_file, analysis)

    print(summary)

    write_summary(output_file, summary)

    print("Summary saved to", output_file)

except FileNotFoundError:
    print("Error: The file was not found. Please check the file name and folder.")
