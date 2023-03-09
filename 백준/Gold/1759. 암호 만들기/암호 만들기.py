#1759 암호 만들기

# 하나 이상의 모음 (a,e,i,o,u)가 퐘되고, 두개 이상의 자음으로 구성되어 있음.
# 알파벳 오름차순으로 구성되어있어야 한다.
# 중복 불가능
from itertools import combinations
L, C = map(int,input().split())

arr = [x for x in input().split()]
arr.sort()
collection_list = ['a','e','i','o','u']

collection = []         #모음
consonant = []          #자음
for i in arr:
    if i in collection_list:
        collection.append(i)
    else:
        consonant.append(i)
tmp = list(combinations(arr,L))

for i in tmp:
    col_cnt =0
    con_cnt = 0
    for j in i:
        if j in collection_list:
            col_cnt +=1
        else:
            con_cnt +=1
    if col_cnt>=1 and con_cnt>=2:
        print(''.join([str(elem)for elem in i]))
  

