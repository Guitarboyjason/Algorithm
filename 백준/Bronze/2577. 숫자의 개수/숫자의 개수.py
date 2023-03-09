a=int(input())
b=int(input())
c=int(input())
d = ""
multi = a*b*c
multi = str(multi)
for i in range(10):
    d = str(i)
    print(multi.count(d))
