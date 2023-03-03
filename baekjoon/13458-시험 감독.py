#응시자 - A
#총감 - B 부총감 - C
#총감은 한명, 필요한 감독관 수는?
N = int(input())
A = input().split()
B, C = map(int,input().split())
sum = 0
for i in A:
    if (int(i) - B) <= 0:
        sum += 1
    elif (int(i) - B)%C == 0 :
        sum += (int(i) - B)//C + 1
    else:
        sum += (int(i) - B)//C + 2
print(sum)
