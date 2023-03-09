def solve(N):
    if N < 10:
        return N
    else:
        if N%10 >= 5:
            return(solve(N//10+1))
        else:
            return(solve(N//10))

N = int(input())
if int(str(N)[0]) == 9 and str(N)[0] != str(solve(N)):
    print(str(solve(N)) + "0"*(len(str(N))))
else:
    print(str(solve(N)) + "0"*(len(str(N))-1))

