from itertools import combinations

collections = list("a,e,i,o,u".split(","))
# print(collections)

L,C = map(int,input().split())
list_collections = []
list_consonant = []

list_input = list(input().split())
# print(list_input)
for c in list_input:
    # print(c)
    if c in collections:
        list_collections.append(c)
    else:
        list_consonant.append(c)

pos_collections = []
pos_consonant = []
for i in range(1,len(list_collections)+1):
    pos_collections.extend(list(combinations(list_collections,i)))

for j in range(2,len(list_consonant)+1):
    pos_consonant.extend(list(combinations(list_consonant,j)))
    
# print(pos_collections)
# print(pos_consonant)
answer = []
for i in range(len(pos_collections)):
    for j in range(len(pos_consonant)):
        tmp = "".join(pos_collections[i]) + "".join(pos_consonant[j])
        if len(tmp) == L:
            answer.append("".join(sorted(tmp)))
            
# print(*sorted(answer))
# answer = list(set(answer))
for ans in sorted(answer):
    print(ans)