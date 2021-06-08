n = int(input())
students_dict = {}

for _ in range(n):
    name, grade = input().split()
    grade = float(grade)
    if name not in students_dict:
        students_dict[name] = []
    students_dict[name].append(grade)

for name, grades in students_dict.items():
    average_grade = sum(grades)/len(grades)
    print(f"{name} ->", end=" ")
    for grade in grades:
        print(f"{grade:.2f}", end=" ")
    print(f"(avg: {average_grade:.2f})")
    
    