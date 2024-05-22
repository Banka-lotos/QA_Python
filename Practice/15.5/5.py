def calculate_average(grades):
    return sum(grades, 0) / len(grades) if grades else "Список оценок пустой"


grades = [6, 7, 9, 6, 10]
average_grade = calculate_average(grades)
print("Средняя оценка:", average_grade)