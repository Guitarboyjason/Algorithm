# n < 10**12
# 1,000,000,000,000
# for 문을 하나만 돌려도 시간 초과
# log(n)만큼 돌려야 가능함
# 근데 결국 n까지 확인을 해서 n이 prime_num인지 확인을 해줘야
# 하지 않나...?
# 그럼 바로 시간 초과인데....
# 계속해서 num을 나누는지 아닌지를 체크해야하는건가
# from collections import deque


# def prime_cnt(num):
#     # prime_num = deque(i for i in range(2, int(num**0.5)+1))
#     prime_num_index = [False, False]+[True for _ in range(2, num+1)]
#     # prime_num = deque(i for i in range(2,int(num**0.5)+1))
#     cnt = num  # 1도 포함 된 것
#     for i in range(2, int(num)+1):
#         if prime_num_index[i] == True:
#             for j in range(1, int(num)//i+1):
#                 if prime_num_index[i*j] == True:
#                     prime_num_index[i*j] = False
#         # if num % node == 0:
#         #     cnt -= num // node #들어간 갯수만큼 빼준다
#     return prime_num_index.count(True)

#     # 여기서 바로 시간초과 뜨지않나...
#     # 아니면 갯수만 포함이니까
#     # 소수들을 검사할 때 배열에 집어 넣고 그 배열에
#     # 계속 참조하면서 갯수를 빼야하나...
#     # print(prime_num_index)
#     # while prime_num


# n = int(input())
# print(prime_cnt(n))
n = int(input())
cnt = n
for i in range(2, round((n**0.5))+1):
    if n % i == 0:
        while n % i == 0:
            n //= i
        cnt *= (1-1/i)
if n > 1:
    cnt *= 1-(1/n)
print(round(cnt))
