
prim_num_list = [False,False]+[True for _ in range(999)]
for i in range(2,1001):
    if prim_num_list[i] == True:
        for j in range(2*i,1001,i):
            prim_num_list[j] = False

# print(prim_num_list)
prim_num_index = []
for index,i in enumerate(prim_num_list):
    if i == True:
        prim_num_index.append(index)
# print(len(prim_num_index))


for _ in range(int(input())):
    num = int(input())
    sum_num_list = [-1,-1,-1]
    try:
        for i in range(len(prim_num_index)):
            sum_num_list[0] = prim_num_index[i]
            for j in range(i,len(prim_num_index)):
                sum_num_list[1] = prim_num_index[j]
                for k in range(j,len(prim_num_index)):
                    sum_num_list[2] = prim_num_index[k]
                    if sum(sum_num_list) == num:
                        print(*sum_num_list)
                        raise()
        print(0)
    except:
        continue