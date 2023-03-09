N,M = map(int,input().split())

DNA_list = [input()for _ in range(N)]
cnt_list = [0,0,0,0]
DNA_kind = ["A","C","G","T"]
diff = 0

for i in range(M):
    for j in DNA_list:
        cnt_list[DNA_kind.index(j[i])] += 1
    # print(cnt_list)
    for index,j in enumerate(cnt_list):
        if j == max(cnt_list):
            print(DNA_kind[index],end="")
            diff += (N-j)
            break
    cnt_list = [0,0,0,0]
print()
print(diff)
