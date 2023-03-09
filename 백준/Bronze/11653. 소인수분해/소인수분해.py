#11653 소인수 분해

def soinsu(N):
    if N ==1:
        return 0
    for i in range(2,N+1):
        if N%i == 0:
            print(i)
            soinsu((int)(N/i))
            return 0
N = int(input())
soinsu(N)
