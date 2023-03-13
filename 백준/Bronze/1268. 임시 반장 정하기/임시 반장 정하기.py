students = int(input())
class_students = [-1]
for student in range(students):
    class_students.append(list(map(int,input().split())))
    
dict_students = dict()

for i in range(1,students+1):
    dict_students[i] = set()
    for j in range(1,students+1):
        if i == j:
            continue
        for k in range(5):
            if class_students[i][k] == class_students[j][k]:
                dict_students[i].add(j)
print(max(dict_students.items(),key=lambda x : len(x[1]))[0])