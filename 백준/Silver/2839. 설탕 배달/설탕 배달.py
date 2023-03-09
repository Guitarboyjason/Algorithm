n=input()
n=int(n)
count=0

while n >= 0:
     if n%5==0:
         print(int (n/5+count))
         break
     else:
         n=n-3
         count=count+1
if n<0:
    print('-1')