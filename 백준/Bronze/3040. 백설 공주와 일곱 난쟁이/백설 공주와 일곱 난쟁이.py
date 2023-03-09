#난쟁이가 쓰고 다니는 모자에 100보다 작응 양의 정수
#일곱 난쟁이의 모자에 쓰여 있는 숫자의 합이 100
from itertools import combinations
arr_nanjang = []
for i in range(9):
    arr_nanjang.append(int(input()))

over = sum(arr_nanjang)
over = over-100
for i in list(combinations(arr_nanjang, 2)):
    if i[0] + i[1] == over:
        for j in arr_nanjang:
            if j != i[0] and j!=i[1]:
                print(j)
        break
