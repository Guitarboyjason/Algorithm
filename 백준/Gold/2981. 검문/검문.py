import sys
input = sys.stdin.readline


def gcd(b1, b2):
    while b2:
        b1, b2 = b2, b1 % b2
    return b1


# print(gcd(5, 2))

N = int(input())
num_list = list(int(input())for _ in range(N))
num_list.sort()
sub_num_list = []
for i in range(N-1):
    sub_num_list.append(num_list[i+1]-num_list[i])

answer = sub_num_list[0]
for i in range(1, len(sub_num_list)):
    answer = gcd(answer, sub_num_list[i])

answer_set = set()
for i in range(2, int(answer**0.5)+1):
    if answer % i == 0:
        answer_set.add(i)
        answer_set.add(answer//i)
answer_list = list(answer_set) + [answer]
answer_list.sort()
print(*answer_list)
