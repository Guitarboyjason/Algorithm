N = int(input())
liquid_list = list(map(int, input().split()))
liquid_list.sort()

max_diff_liquid = 2000000001
liquid_a = -1
liquid_b = -1
j = N-1
i = 0
# before_blended = -1
while i < j:

    if abs(liquid_list[i] + liquid_list[j]) < abs(max_diff_liquid):
        max_diff_liquid = liquid_list[i] + liquid_list[j]
        liquid_a, liquid_b = liquid_list[i], liquid_list[j]
    if liquid_list[i] + liquid_list[j] < 0:
        i += 1
    else:
        j -= 1
print(liquid_a, liquid_b)
