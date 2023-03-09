N,k = map(int,input().split())
stu = list(map(int,input().split()))

stu.sort(reverse=True)

print(stu[k-1])