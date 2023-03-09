from itertools import combinations
line = input()
while line != "0":
    k, list = line.split()[0], line.split()[1:]
    for i in combinations(list, 6):
        print(*i)
    print()
    line = input()
