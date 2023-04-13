N,S = map(int,input().split())
arr = list(map(int,input().split()))

summary_arr = [0]
for i in arr:
    tmp = summary_arr.copy()
    for j in tmp:
        summary_arr.append(j+i)
print(summary_arr[1:].count(S))