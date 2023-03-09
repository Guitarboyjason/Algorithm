N = int(input())
F = int(input())

tmp_N = int(N/100) * 100

for i in range(100):
    if (tmp_N+i) % F == 0:
        if i < 10:
            print("0"+str(i))
            break
        else:
            print(i)
            break