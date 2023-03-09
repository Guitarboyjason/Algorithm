num = int(input())
list = []
list.extend(input().split())
real_list = []
for i in list :
    real_list.append(int(i))
real_list.sort()
max = real_list[num-1]
avg = sum(real_list)/max*100/num
print("%.2f"%avg)
