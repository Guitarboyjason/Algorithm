run = 1
while run:
    n = int(input())
    if n == -1:
        run = 0
        break
    else:
        arr = []
        for i in range(1,int(n/2)+1):
            if n % i == 0:
                arr.append(i)
        if sum(arr) == n:
            print("%d = "%n,end="")
            for i in arr:
                if i != max(arr):
                    print("%d + "%i,end="")
                else:
                    print("%d"%i)
        else:
            print("%d is NOT perfect."%n)
