
#일단 무조건 brown이 yello보다 4개는 많다
#그리고 4개를 빼고 난 뒤에도 (가로 + 세로) * 2 만큼 차이가 난다.
# 항상 가로 >= 세로이므로 가능한 숫자중 고르면 되겠다.
def solution(brown,yellow):
    brown -= 4
    brown /= 2
    arr = []
    for i in range(1,yellow+1):
        if yellow % i == 0:
            arr.append([yellow//i,i])
    print(arr)
    for i in arr:
        if i[0] + i[1] == brown:
            return [max(i)+2,min(i)+2]


print(solution(10,2))
