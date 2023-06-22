# O Z N E T W R

# ZERO  #
# ONE
# TWO   #
# THREE #
# FOUR  #
# FIVE
# SIX   #
# SEVEN
# EIGHT #
# NINE


# Z => 0, X -> 6 , W -> 2 , G -> 8, U -> 4, R -> 3

for T in range(1,int(input())+1):
    S = list(input())
    num = []
    while "Z" in S:
        num.append(0)
        for i in list("ZERO"):
            S.remove(i)
    while "X" in S:
        num.append(6)
        for i in list("SIX"):
            S.remove(i)
    while "W" in S:
        num.append(2)
        for i in list("TWO"):
            S.remove(i)
    while "G" in S:
        num.append(8)
        for i in list("EIGHT"):
            S.remove(i)
    while "U" in S:
        num.append(4)
        for i in list("FOUR"):
            S.remove(i)
    while "R" in S:
        num.append(3)
        for i in list("THREE"):
            S.remove(i)
    
    # 하고 남은 애들중 O -> 1, F -> 5, S -> 7, 나머지 9
    while "O" in S:
        num.append(1)
        for i in list("ONE"):
            S.remove(i)
    while "F" in S:
        num.append(5)
        for i in list("FIVE"):
            S.remove(i)
    while "S" in S:
        num.append(7)
        for i in list("SEVEN"):
            S.remove(i)
    while S:
        num.append(9)
        for i in list("NINE"):
            S.remove(i)
    num.sort()
    print(f"Case #{T}: ",end="")
    for i in num:
        print(i,end="")
    print()
