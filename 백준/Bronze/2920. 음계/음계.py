music_line = list(map(int,input().split()))

answer = "mixed"

for i in range(1,9):
    if music_line[i-1] != i:
        break
else:
    answer = "ascending"
for i in range(1,9):
    if music_line[-i] != i:
        break
else:
    answer = "descending"
    
print(answer)
    