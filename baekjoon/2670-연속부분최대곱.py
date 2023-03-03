def max_mult(result1,arr) :
    #비교할거야 포함한것과 안한것을
    if len(arr) == 1:
        return max(result1*arr[0], result1)
    if result1 != 1: #시작 한경우
        return max(max_mult(result1*arr[0],arr[1:]),result1)
    else:   #시작 안한경우
        return max(max_mult(result1*arr[0],arr[1:]),\
                   max_mult(result1,arr[1:]))
N = int(input())
arr = []
for i in range(N):
    arr.append(float(input()))
if max(arr) <= 1:
    print("%.3f"%max(arr))
else:
    print("%.3f"%max_mult(1,arr))


