N = int(input())
map = str(input())


count = 1
for i in range(len(map)):
    if i == 0 and map[i] == "W" or i == len(map)-1 and map[i] == "E":
        count += 1
    elif i != len(map)-1 and map[i] == "W" and map[i+1] == "E" :
        count += 1
print(count)