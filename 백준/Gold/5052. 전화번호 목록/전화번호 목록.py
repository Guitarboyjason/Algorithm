# 일관성이 없다 -> 한 번호가 다른 번호의 접두어인 경우

# dictionary형식으로 진행을 하는데 끝났으면 done flage를 True로 바꿔준다
import sys
input = sys.stdin.readline

for test_case in range(int(input())):
    n = int(input().rstrip())
    numbers = [input().rstrip() for _ in range(n)]
    numbers.sort()
    num_dict = {"done_flag" : False}
    
    consistency = True
    for num in numbers:
        tmp = num_dict
        for c in num:
            if c not in tmp:
                tmp[c] = {"done_flag" : False}
            if tmp["done_flag"] == True:
                consistency = False     # 잘못됨을 인지
                break
            tmp = tmp[c]
        
        if not consistency:
            break
        # 마지막에 도착
        tmp["done_flag"] = True
        # print(num_dict)

    if consistency:
        print("YES")
    else:
        print("NO")