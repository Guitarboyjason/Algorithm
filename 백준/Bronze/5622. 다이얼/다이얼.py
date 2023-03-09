list = ["ABC","DEF","GHI","JKL","MNO","PQRS","TUV","WXYZ"]
S = input()
sum = 0
for i in S:
    for j in range(len(list)):
        for k in list[j]:
            if k == i:
                sum+= j+3
print(sum)
