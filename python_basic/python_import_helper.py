def calculate_homework(homework_assignments):
    total_score = 0
    for score in homework_assignments.values():
        total_score += score
    final_grade = total_score / len(homework_assignments)
    print(final_grade)