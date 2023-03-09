#수의 각 자리수를 내림차순으로 정렬하자

#그냥 카운트로 매겨서
#숫자를 새로 만드는게 좋을듯

N = input()
arr = [0] * 10
for i in N:
    arr[int(i)] += 1

answer = ""
for i in range(9,-1,-1):
    answer += str(i) * arr[i]
print(answer)