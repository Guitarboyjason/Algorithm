# 우선순위를 무시하고 앞에서부터 진행이 된다.
# 나눗셈은 몫만
import sys
input = sys.stdin.readline

operation_list = ["+","-","*","//"]
def calculator(nums,operations):
    if len(nums)==1:
        return [nums[0]]
    results = []
    # if operations[0] != 0:
        # tmp_op = operations
    for idx,i in enumerate(operations):
        if i != 0:
            tmp_result = eval(str(nums[0])+operation_list[idx]+str(nums[1]))
            if idx == 3 and nums[0]<0 and nums[1]>0:
                tmp_result = -(abs(nums[0])//abs(nums[1]))
            tmp_ops = []
            tmp_ops = operations[:idx]+[operations[idx]-1]+operations[idx+1:]
            results.extend(calculator([tmp_result]+nums[2:],tmp_ops))
    return results
N = int(input())
nums = list(map(int,input().split()))
operations = list(map(int,input().split()))

# 완전 탐색 가능할 것 같음
result = calculator(nums,operations)
print(max(result))
print(min(result))
