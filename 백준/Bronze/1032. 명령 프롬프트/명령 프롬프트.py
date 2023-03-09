N = int(input())

answer = ""

for i in range(N):
    file_name = input()
    if i == 0:
        answer = file_name
    else:
        for j in range(len(answer)):
            if answer[j] != '?' and file_name[j] != answer[j]:
                answer = list(answer)
                answer[j] = "?"
                answer = ''.join(answer)
print(answer)