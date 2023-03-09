T = int(input())
arr_button = [300,60,10]
arr_button_print = []
if T % 10 != 0:
    print(-1)
else:
    while T != 0:
        for i in arr_button:
            count = 0
            if T >= i:
                count = T // i
                T -= count * i
            arr_button_print.append(count)
for i in arr_button_print:
    print("%d" %i,end=' ')
