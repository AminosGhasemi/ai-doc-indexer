def main():
    def approx_eq(a: float, b: float, tol: float = 1e-6) -> bool:
        return abs(a - b) < tol

    students = [
        {"name": "Amin", "grades": [80, 90, 70]},
        {"name": "Sara", "grades": [60, 75, 85]},
        {"name": "Ali", "grades": [95, 88, 91]},
    ]

    # average_grade
    assert approx_eq(average_grade(students[0]), 80.0)  # (80+90+70)/3
    assert approx_eq(average_grade(students[1]), 73.333333)  # (60+75+85)/3

    # class_average: all grades sum / count
    # Amin: 80+90+70 = 240
    # Sara: 60+75+85 = 220
    # Ali: 95+88+91 = 274
    # total = 734, count = 9 -> 734/9 ≈ 81.555555...
    assert approx_eq(class_average(students), 734 / 9)

    # unique_grades
    expected_unique = {60, 70, 75, 80, 85, 88, 90, 91, 95}
    assert unique_grades(students) == expected_unique

    # top_students
    top2 = top_students(students, n=2)
    assert len(top2) == 2
    assert top2[0]["name"] == "Ali"  # highest average
    assert top2[1]["name"] == "Amin"  # second highest

def average_grade(student: dict) -> float:
    sum = 0
    count = 0
    for i in range(len(student["grades"])):
        sum += student["grades"][i]
        count += 1

    # mean of student["grades"].
    return sum / count

def class_average(students: list[dict]) -> bool:
    sum = 0
    count = 0
    for i in range (len(students)):
        for j in range (len(students[i]["grades"])):
            sum += students[i]["grades"][j]
            count += 1

    # class_average: all grades sum / count
        return sum / count

def top_students(students: list[dict], n: int = 3) -> list[dict]:
     top: list = []
     for i in range(len(students)):
         top.append((average_grade(students[i]), students[i]))
         top.sort(key=lambda x: x[0], reverse=True)
    # return the n students with highest average grade, as a list of dicts (you can sort by average).
        return [student for _, student in top[:n]]

def unique_grades(students: list[dict]) -> set[int]:
    ...

if __name__ == "__main__":
    main()