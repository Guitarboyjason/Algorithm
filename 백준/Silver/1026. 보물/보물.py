n = int(input())
arr_A = [int(x) for x in input().strip().split()]
arr_B = [int(x) for x in input().strip().split()]

arr_A.sort()
arr_B.sort(reverse=True)

result = 0
for i in range(0,len(arr_A)):
    result += arr_A[i] * arr_B[i]

print(result)
