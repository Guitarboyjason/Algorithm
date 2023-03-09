T = int(input())
cnt_0 = 0
cnt_1 = 0
f_0 = [-1]*(41)
f_1 = [-1]*(41)
f_0[0] = 1
f_0[1] = 0
f_1[0] = 0
f_1[1] = 1
def f_arr(num):
    return f_0[num], f_1[num]

def fib(num):
    if f_0[num] != -1:
        return f_arr(num)
    else:
        tmp_0_a, tmp_1_a = fib(num-1)
        tmp_0_b, tmp_1_b = fib(num-2)
        f_0[num] = tmp_0_a + tmp_0_b
        f_1[num] = tmp_1_a + tmp_1_b
        return f_arr(num)

for _ in range(T):
    n = int(input())
    

    a,b = fib(n)
    
    print(a, b)
