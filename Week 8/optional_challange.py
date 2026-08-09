# Week 8 Optional Independent Challenge
# Sorted ranking from highest score to lowest score
# Completed without ChatGPT or external help

def print_ranking(students):
    ranking = []

    for student, score in students.items():
        ranking.append((student, score))

    ranking.sort(key=lambda item: item[1], reverse=True)

    print("Ranking:")
    position = 1

    for student, score in ranking:
        print(str(position) + ".", student, "-", score)
        position = position + 1


students = {
    "Anna": 88,
    "Erik": 62,
    "Sara": 91,
    "Jonas": 54,
    "Maria": 76
}

print_ranking(students)
