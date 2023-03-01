# 1     0       1
# 2     1 0     2
# 3     1 0     2
# 4     2 1 0   3
# 5     2 1 0   3
# 6     3 1 0   3
# 7     3 1 0   3
import math
# print(math.log(10,2))
# print(math.sqrt(2))
list_multiple_2 = [2**i for i in range(19)]
# print(list_multiple_2)
n = int(input())
for i in list_multiple_2[::-1]:
    if n >= i:
        answer = int(math.log(i,2))+1
        print(answer)
        if n == 1:
            complexity = 0
        else:
            complexity = int(math.log(answer,n))
        if complexity > 3:
            print(4)
        else:
            print(complexity)
        break