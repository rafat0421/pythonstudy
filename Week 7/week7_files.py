# Week 7 - File Handling and Mini-Program Design

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

    keyword_count = 0
    word_frequencies = {}

    for word in cleaned_words:
        if word == keyword:
            keyword_count = keyword_count + 1

        word_frequencies[word] = word_frequencies.get(word, 0) + 1

    analysis = {
        "line_count": len(lines),
        "word_count": len(cleaned_words),
        "keyword": keyword,
        "keyword_count": keyword_count,
        "word_frequencies": word_frequencies
    }

    return analysis


def create_summary(file_name, analysis):
    summary = ""
    summary = summary + "File analyzed: " + file_name + "\n"
    summary = summary + "Lines: " + str(analysis["line_count"]) + "\n"
    summary = summary + "Words: " + str(analysis["word_count"]) + "\n"
    summary = summary + "Keyword '" + analysis["keyword"] + "': " + str(analysis["keyword_count"]) + "\n"

    return summary


def write_summary(file_name, summary):
    with open(file_name, "w") as file:
        file.write(summary)


input_file = "sample.txt"
output_file = "output.txt"
keyword = "python"

try:
    text = read_file(input_file)
    analysis = analyze_text(text, keyword)
    summary = create_summary(input_file, analysis)

    print(summary)

    write_summary(output_file, summary)

    print("Summary saved to", output_file)

except FileNotFoundError:
    print("Error: The file was not found. Please check that sample.txt is in the same folder as this Python file.")
