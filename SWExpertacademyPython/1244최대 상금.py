import sys
sys.stdin = open('sources/input.txt')


def change(numbers, cnt):
    global result
    tmp = "".join(numbers)
    if int(tmp) in result[cnt]:
        return
    else:
        result[cnt].append(int(tmp))

    if cnt == 0:
        return
    n = len(numbers)

    for i in range(n):
        for j in range(i+1, n):
            numbers[i], numbers[j] = numbers[j], numbers[i]

            change(numbers, cnt-1)

            numbers[i], numbers[j] = numbers[j], numbers[i]


T = int(input())

for i in range(1, T+1):
    tmp, cnt = input().split()

    numbers = list(tmp)
    result = [[]for _ in range(int(cnt)+1)]

    change(numbers, int(cnt))

    print("#{} {}".format(i, max(result[0])))
