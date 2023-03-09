# 세 변의 길이가 모두 같은 경우 : Equilateral
# 두 변의 길이만 같은 경우 : Isosceles
# 세 변의 길이가 모두 다른 경우 : Scalene

lines = list(map(int,input().split()))
while lines[0] or lines[1] or lines[1]:
    lines.sort()
    line_counter = set(lines)
    if len(line_counter) == 1:
        print("Equilateral")
    else:
        if sum(lines[:2]) <= lines[-1]:
            print("Invalid")
        elif len(line_counter) == 2:
            print("Isosceles")
        else:
            print("Scalene")
    lines = list(map(int,input().split()))