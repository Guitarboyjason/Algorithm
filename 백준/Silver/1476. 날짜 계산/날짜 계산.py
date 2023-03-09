

E,S,M = map(int,input().split())

cnt_list = [E,S,M]

year_limit = [15,28,19]
max_year = 7980
while cnt_list[0] != cnt_list[1] or cnt_list[0] != cnt_list[2]:
    min_index = cnt_list.index(min(cnt_list))
    cnt_list[min_index] += year_limit[min_index]
    
print(cnt_list[0])
