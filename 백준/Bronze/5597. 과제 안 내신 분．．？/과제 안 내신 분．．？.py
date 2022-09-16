students = [i for i in range(1,31)]

for _ in range(28):
    student = int(input())
    students.remove(student)

print(min(students))
print(max(students))