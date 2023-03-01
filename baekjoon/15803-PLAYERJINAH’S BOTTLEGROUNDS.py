teams = [list(map(int,input().split()))for _ in range(3)]

# 직선이 되면 안된다. 이 말은 두 수를 뽑아 기울기를 확인 하는 것.
# 모든 기울기가 같으면 진다.

teams.sort()
# print(teams)
if (teams[2][0]-teams[0][0])*(teams[1][1]-teams[0][1]) ==\
    (teams[1][0]-teams[0][0])*(teams[2][1]-teams[0][1]):
        print("WHERE IS MY CHICKEN?")
else:
    print("WINNER WINNER CHICKEN DINNER!")