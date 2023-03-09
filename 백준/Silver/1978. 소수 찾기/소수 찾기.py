prime_num = [False,False] + [True for _ in range(999)]

for index,i in enumerate(prime_num):
    if i == True:
        for j in range(index*2,1001,index):
            prime_num[j] = False
        



N = int(input())
arr = list(map(int,input().split()))
cnt = 0
for i in arr:
    if prime_num[i] == True:
        cnt += 1
        
print(cnt)