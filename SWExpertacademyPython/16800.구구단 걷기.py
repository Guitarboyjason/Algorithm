def find_elements(N:int):
    # if N**0.5 < 2:
    #     return [1,N]
    for i in range(int(N**0.5),0,-1):
        if N % i == 0:
            return [i,N//i]

for test_case in range(1,int(input())+1):
    N = int(input())
    a,b = find_elements(N)
    print(f"#{test_case} {a+b-2}")
    