N, M = map(int,input().split())

dots = list(map(int,input().split()))
lines = []
for _ in range(M):
    lines.append(list(map(int,input().split())))

dots.sort()

def find_start_index(dots,start_index,end_index,line):
    if start_index > end_index:
        return end_index
    if dots[start_index] >= line[0]:
        return start_index
    else:
        mid = (start_index + end_index) // 2
        if dots[mid] == line[0]:
            return mid
        elif dots[mid] > line[0]:
            return find_start_index(dots,start_index,mid-1,line)
        else:
            return find_start_index(dots,mid+1,end_index,line)

def find_end_index(dots,start_index,end_index,line):
    if start_index > end_index:
        return end_index
    if dots[end_index] <= line[1]:
        return end_index
    else:
        mid = (start_index + end_index) // 2
        if dots[mid] == line[1]:
            return mid
        elif dots[mid] > line[1]:
            return find_end_index(dots,start_index,mid-1,line)
        else:
            return find_end_index(dots,mid+1,end_index,line)

# print(find_start_index(dots,0,len(dots)-1,lines[0]))
for i in lines:
    count = find_end_index(dots,0,len(dots)-1,i) - find_start_index(dots,0,len(dots)-1,i)
    if count != 0:
        print(count+ 1)
    else:
        print(count)

