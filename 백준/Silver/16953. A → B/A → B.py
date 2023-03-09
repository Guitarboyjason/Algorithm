
# 2를 곱한다.
# 1을 수의 가장 오른쪽에 추가한다.

# 만약 B의 마지막 숫자가 1이라면 무조건 마지막 연산은 2번째 연산
# 마지막 숫자가 1이 아닌 홀수라면 무조건 만들 수 없음.
# 나머지 다른 경우에는 짝수인 경우만 남으므로 B의 끝자리가 1이 될 때 까지
# 나누기 2를 진행한다.
# 끝자리가 1이 되면 다시 2번 연산

A, B = map(int, input().split())
cnt = 0
while A != B:
    cnt += 1
    # print(B)
    if A > B:
        cnt = -2
        break
    if B % 10 != 1 and B % 2 == 1:
        cnt = -2
        break
    if B % 10 == 1:
        B = B//10
    else:
        B = B // 2

print(cnt+1)
