def beeHouse(N):
    sum = 1
    for i in range(0,N):
        sum += i*6
        if sum>=N:
            return i+1
            

N = int(input())
print(beeHouse(N))