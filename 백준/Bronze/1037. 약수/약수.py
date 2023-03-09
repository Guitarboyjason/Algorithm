N = int(input())
list = input().split()
for i in range(len(list)):
        list[i] = int(list[i])
print(min(list)*max(list))
    
