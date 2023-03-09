num = int(input())
realnum = num
count = 0
while True :
    num_1 = num
    num = num // 10
    num_1 = num_1 % 10
    base_new = num + num_1
    base_1 = base_new % 10
    base_new = base_new // 10
    num = num_1 * 10 + base_1
    count += 1
    if num == realnum :
        break
print(count)