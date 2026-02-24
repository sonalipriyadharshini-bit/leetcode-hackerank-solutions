if __name__ == '__main__':
    students = []
    grades = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
        grades.append(score)
    unique_grades = sorted(set(grades))
    second_lowest_grade = unique_grades[1]
    second_lowest_students = [s[0] for s in students if s[1] == second_lowest_grade]
    second_lowest_students.sort()
    for name in second_lowest_students:
        print(name)
