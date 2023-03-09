num = int(input())
for i in range(num) :
    list = []
    real_list = []
    list.extend(input().split())
    num_list = int(list[0])
    for j in range(1,num_list+1):
        real_list.append(int(list[j]))
    avg = sum(real_list) / num_list
    count = 0
    for j in range(num_list):
        if real_list[j] > avg:
            count += 1
    percent = count / num_list * 100
    print("%.3f%%"%percent)
