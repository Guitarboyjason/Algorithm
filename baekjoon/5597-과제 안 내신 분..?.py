students = [True] + [False for i in range(31)]
for _ in range(28):
    check = int(input())
    students[check] = True
    
# for i in students:
#     if i != 0:
#         print(i)
print(students.index(False))
students.remove(False)
print(students.index(False)+1)