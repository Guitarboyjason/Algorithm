# 12865-평범한 배낭.py

# 배낭에 최대한의 가치를 지니게 들어야 한다.

# def find_max_value(arr_thing,weight,value):
#     if len(arr_thing) == 0:
#         return value
#     elif weight>= arr_thing[0][0]:
#         return max(find_max_value(arr_thing[1:],weight-arr_thing[0][0],value+arr_thing[0][1]),
#         find_max_value(arr_thing[1:],weight,value))
#     else:
#         return value

def find_max_value_reverse(arr_thing,weight,value):
    if len(arr_thing) == 0:
            return value
    elif weight>= arr_thing[0][0]:
        return max(find_max_value_reverse(arr_thing[1:],weight-arr_thing[0][0],value+arr_thing[0][1]),
        find_max_value_reverse(arr_thing[1:],weight,value))
    else:
        return value

N , K = map(int,input().split())


arr_thing=[]
for _ in range(N):
    arr_thing.append(list(map(int,input().split())))

arr_thing.sort(key=lambda x:x[1],reverse=True)
arr_thing.sort(key=lambda x:x[0],reverse=True)

print(find_max_value_reverse(arr_thing,K,0))


# 물건 1을 가져 가거나 말거나
# 물건 2를 가져 가거나 말거나
# 이게 가지는 의미는?
# 1을 가져 간다고 했을 때, (물건들을 무게 내림차순으로 정렬을 했다면)
# 1을 가져감으로 인해서 선택을 못하는 경우들이 생기게 된다.
# 일단 무게가 적은 순으로 가져간다면 많이 가져갈 수 있다.
# 다이나믹 프로그래밍으로 풀려면 많은 중복이 존재하는 경우 중복을 줄이기 위해
# 노력해야 한다.
# 어떤 중복들이 존재하는 걸까.
# 

# 아니면 bottom-up 방식으로 풀려고 노력 하는것도 괜찮은 것 같은데...
# 