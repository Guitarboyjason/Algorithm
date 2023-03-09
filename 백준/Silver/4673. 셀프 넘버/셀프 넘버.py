def d(n):
    # new_num = n + n//1000 + (n-(n//1000*1000))//100 + (n-(n-(n//1000*1000))//100*100)//10 + n%10
    # return new_num
    sum = n + n % 10
    if len(str(n)) == 4:
        a = n // 1000
        sum += a
        b = (n - a*1000) // 100
        sum += b
        c = ((n - a*1000) - b*100) // 10
        sum += c
    elif len(str(n)) == 3:
        b = n // 100
        sum += b
        c = (n - b*100) // 10
        sum += c
    elif len(str(n)) == 2:
        n = n // 10
        sum += n
    else :
        pass
    return sum
list_all = []
for i in range(1,10001):
    list_all.append(i)
for i in range(1,10001):
    if d(i) in list_all :
        del list_all[list_all.index(d(i))]
for i in list_all:
    print(i)
