from collections import deque

def solution(operations):
    arr = []
    for i in operations:
        if i[0] == "I":
            arr.append(int(i[2:]))
            arr.sort()
        else:
            if len(arr) == 0:
                continue
            if len(i) == 3:
                arr.pop()
            else:
                arr = arr[1:]
    if len(arr) == 0:
        return [0,0]
    else:
        return [arr[0-1],arr[0]]
operations = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
print(solution(operations))
