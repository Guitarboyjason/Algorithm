# 0부터 9까지의 숫자중 최대값을 구하면 되겠네
# 근데 예외가 6과 9는 합쳐서 절반 나누는 갯수만큼 생각해야함

N = int(input())
arr = [0 for _ in range(10)]

while N:
    arr[N%10] += 1
    N = N//10

arr[6] += arr.pop()
if arr[6] % 2 == 0:
    arr[6] = arr[6]//2
else:
    arr[6] = arr[6] // 2 + 1

print(max(arr))
