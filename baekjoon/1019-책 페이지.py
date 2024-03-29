# 999까지를 확인한다고 했을 때 1~ 999 라고 생각하지 말고
# 000 ~ 999 까지라고 생각을 하면 계산하기 편함
# 숫자 자체는 3 * 1000 개이므로 3000 개 / 10 이면
# 각 숫자는 300개씩 갖고 있는 것인데,
# 특별히 0의 숫자를 계산해야 한다.
# 000 -> 3개
# 00x -> 2 * 9개
# 0xx -> 1 * 90개
# => 90 + 18 + 3 = 111
# => 0 만 갯수가 300 - 111이 된다.

# 반면 만약 숫자가 3000과 같이 주어진다면,
# 000~999 전체 를 총 세번한다고 생각하면 된다.
# 그럼 0은 900 - 111 이고 나머지는 전부 900이 되는데
# 1, 2는 + 999 씩을 더하게 된다.
# 이게 2999까지임 3000은 계산 따로.

# 만약 숫자가 3500 이라면,
# 위와 같은 과정을 똑같이 거치고,
# 500만큼을 진행하면 되는데
# 00 ~ 99 가 5번 진행되면 된다.
# 숫자들은 100 * 2 * 5 / 10 으로 100개씩 더해지게 되는데,
# 500보다 앞자리인 3을 + 500 + 1만큼 더해주면 됨

# 3540이라면
# 앞의 내용들 + 0 ~ 9  * 4 에다
# 3과 5를 각각 40 + 1씩 더해줌


N = int(input())
N_length = len(str(N))

arr_cnt = [0] * 10
while N_length != 0:
    for i in range(10):
        arr_cnt[i] += int(10**(N_length-1) * (N // 10**(N_length-1)) * (N_length) / 10)
    tmp = N // 10**(N_length-1)

    # 1 2 3 4 한테 각각 좀 줘야하는데
    while tmp != 0:
        arr_cnt[tmp % 10] += 10**(N_length-2)
        tmp = tmp// 10
    N_length -= 1

# 0 빼는건 마지막에 할까

print(arr_cnt)


# 10**(len-1)   #   자리수 -1
