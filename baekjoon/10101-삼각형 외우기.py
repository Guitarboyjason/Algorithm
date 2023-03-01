angles = [int(input())for _ in range(3)]
angle_counter = set(angles)
if len(angle_counter) == 1 and angles[0] == 60:
    print("Equilateral")
elif sum(angles) == 180 :
    if len(angle_counter) == 2:
        print("Isosceles")
    else:
        print("Scalene")
else:
    print("Error")