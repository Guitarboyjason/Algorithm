
# 연속된 배열에서 같은 값을 가지는 갯수를 구하면 됨.
# 어차피 N 갯수랑 그레이드 수 얼마 안되는데 다 확인해보면 안되나

N = int(input())
arr_grade = []
max_cnt_grade = [-1]
for _ in range(N):
    g1, g2 = map(int,input().split())
    arr_grade.append([g1,g2])
cnt = 0
tmp = 0
for i in range(1,6):
    for j in arr_grade:
        if i in j:
            cnt += 1
            if cnt > tmp:
                tmp = cnt

        else:
            if cnt > tmp:
                tmp = cnt
            cnt = 0
    max_cnt_grade.append(tmp)
    cnt = 0
    tmp = 0
print(max(max_cnt_grade),max_cnt_grade.index(max(max_cnt_grade)))
