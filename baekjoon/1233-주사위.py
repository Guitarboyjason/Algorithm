from collections import Counter
S1,S2,S3 = map(int,input().split())
sum_list = [sum([i,j,k]) for i in range(1,S1+1) for j in range(1,S2+1) for k in range(1,S3+1)]
print(max([i for i in Counter(sum_list).items()],key=lambda x : x[1])[0])