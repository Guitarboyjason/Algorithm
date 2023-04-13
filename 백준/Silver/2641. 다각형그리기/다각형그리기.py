n = int(input())

base = list(map(int,input().split()))
answer_perm = [base[i:]+base[:i] for i in range(n)]
for i in range(n):
    answer_perm.append(list(reversed([(j+1)%4+1 for j in answer_perm[i]])))

sample_count = int(input())
answer = []
for count in range(sample_count):
    tmp = list(map(int,input().split()))
    if tmp in answer_perm:
        answer.append(tmp)


print(len(answer))
for i in answer:
    print(*i)
    