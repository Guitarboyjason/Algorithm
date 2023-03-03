#x kg, y cm => (x,y)
#몸무게와 키가 더 크다면 덩치가 더 크다고 한다.
#각 사람의 덩치 등수는 자신보다 더 큰 덩치의 사람의 수로 정해진다.

N = int(input())
student = []
for _ in range(N):
    x,y = map(int,input().split())
    student.append([x,y])
for i in student:
    cnt = 0
    for j in student:
        if i[0] < j[0] and i[1] < j[1]:
            cnt += 1
    print(cnt+1,end=" ")
