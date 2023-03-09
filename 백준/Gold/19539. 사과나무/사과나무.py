N = int(input())
heights = list(map(int,input().split()))

if sum(heights)% 3 != 0:
    print("NO")
else:
    cnt_2 = 0
    for height in heights:
        if height >= 2:
            cnt_2 += height//2
            
    if cnt_2 < sum(heights)//3:
        print("NO")
    else:
        print("YES")