arr = [-1]*26

S = input()
for i in range(len(S)):
    if arr[int(ord(S[i]))-97] == -1:
        arr[int(ord(S[i]))-97] = i
for i in arr:
    print(i,end=' ')
    
