num_list = []
for i in range(1,51):
    num_list.extend(list(i for j in range(i)))
# print(num_list)
start, end = map(int,input().split())
print(sum(num_list[start-1:end]))
