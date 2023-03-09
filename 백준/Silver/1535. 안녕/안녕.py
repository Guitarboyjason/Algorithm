# 세준이 생각해준 사람 N명
# 1 ~ N
# i번 사람에게 인사를 하면 L[i]만큼 체력을 잃음, J[i]만큼 기쁨을 얻음
# 각각에게 한번만 말할 수 있다.

# 주어진 체력 내에서 최대한의 기쁨을 느껴라.
# 체력 : 100, 기쁨 : 0
# 체력이 0이되면 안된다.

N = int(input())

arr_L = list(map(int,input().split()))
arr_J = list(map(int,input().split()))

def max_delight(health, delight,arr_L,arr_J):
    if health <= 0:
        return 0
    elif len(arr_L) == 0:
        return delight
    else:
        return max(max_delight(health-arr_L[0],delight+arr_J[0],arr_L[1:], arr_J[1:]),\
                   max_delight(health,delight,arr_L[1:],arr_J[1:]))
print(max_delight(100, 0 , arr_L,arr_J))

