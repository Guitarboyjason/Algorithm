# 일직선으로 움직인다
# 벽이나 방문한 지역, 장애물을 만날 경우 지정한 다음 방향으로 움직인다.
# 지정한 다음 방향이 없다면 맨 처음 방향으로 돌아가서 반복한다.
# 움직일 수 없는 경우 멈춘다.
# R이 세로
def can_move(movement,map,position):
    if movement == 1:
        if position[0]-1 >= 0:
            if map[position[0]-1][position[1]] == '*':
                map[position[0]-1][position[1]] = 'x'
                return True
    elif movement == 2:
        if position[0]+1 <= R-1:
            if map[position[0]+1][position[1]] == '*':
                map[position[0]+1][position[1]] = 'x'
                return True
    elif movement == 3:
        if position[1]-1 >= 0:
            if map[position[0]][position[1]-1] == '*':
                map[position[0]][position[1]-1] = 'x'
                return True
    else:
        if position[1]+1 <= C-1:
            if map[position[0]][position[1]+1] == '*':
                map[position[0]][position[1]+1] = 'x'
                return True
    return False


R,C = map(int,input().split())
k = int(input())
k_position = [list(map(int,input().split()))for _ in range(k)]

robot_map = [['*']*C for _ in range(R)]
robot_position = list(map(int,input().split()))
robot_map[robot_position[0]][robot_position[1]] = 0
for i in k_position:
    robot_map[i[0]][i[1]] = 'x'

movement = list(map(int,input().split()))

movement_index = 0
while True:
    notfound = True
    direction = 0
    for i in range(movement_index , 4):
        if can_move(movement[i],robot_map,robot_position):
            direction = movement[i]
            movement_index = i
            notfound = False
            break
    if notfound:
        for i in range(movement_index):
            if can_move(movement[i],robot_map,robot_position):
                direction = movement[i]
                movement_index = i
                break

    if direction == 1:
        robot_position[0] = robot_position[0]-1
    elif direction == 2:
        robot_position[0] = robot_position[0]+1
    elif direction == 3:
        robot_position[1] = robot_position[1]-1
    elif direction == 4:
        robot_position[1] = robot_position[1]+1
    else:
        break

print(robot_position[0],robot_position[1])

