#18870-좌표압축_2.py

import sys
input = sys.stdin.readline

N = int(input())
X_list = list(map(int,input().split()))
#무조건 이견 없이 확정
#for문을 두개 돌리는게 오바인듯?
##아니 하나만 돌렸는데도 왜 시간 초과가 뜨는거야 진짜 이해 할 수가 없네
##index 함수에 문제가 있는듯? 처음부터 쭉 찾아 나가서 아마 시간 초과가 나오는 것 같은데
##그럼 어떻게 더 작다는 걸확인 할 수 있는거지
##아니면 sorted함수 자체가 시간이 오래 걸리나?
sorted_X_list = sorted(list(set(X_list)))

dic = {sorted_X_list[i] : i for i in range(len(sorted_X_list))}

for i in X_list:
    print(dic[i],end = " ")
    # counter = 0
    # for j in sorted_X_list:
    #     if i <= j:
    #         break
    #     counter += 1
    # print(counter,end= " ")


