T = int(input())
for i in range(1,T+1):
    S = input()
    before= ""
    count = 0
    for j in S:
        if before == "(" or before == "|" :
            if j == ")":
                count += 1
            if before == "(" and j == "|":
                count += 1
        before = j
    print(f"#{i} {count}")
