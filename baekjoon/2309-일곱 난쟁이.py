#일곱 난쟁이의 키의 합이 100
#아홉 난쟁이의 키는 모두 다름
#가능한 정답이 여러가지인 경우 아무거나 출력
#키를 오름차순으로 출력
from itertools import combinations

arr=[]
sum_arr = 0
for i in range(9):
    num = int(input())
    arr.append(num)
    sum_arr += num
arr.sort()
find = sum_arr - 100    # 아닌 난쟁이 두 키의 합

for i in list(combinations(arr,2)):
    if i[0] + i[1] == find:
        for j in arr:
            if j != i[0] and j != i[1]:
                print(j)
        break


