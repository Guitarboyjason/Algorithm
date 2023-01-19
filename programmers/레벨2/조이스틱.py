

def solution(name):
    count = 0
    min_move = len(name)-1
    for index,i in enumerate(name):
        count += min(ord(i) - ord('A'), ord('Z') - ord(i) + 1)

        next = index + 1
        while(next < len(name) and name[next] == 'A'):
            next += 1

        min_move = min([min_move, 2*index +len(name) - next,index + 2*(len(name) - next)])

    count += min_move
    return count

print(solution("JEROEN"))
