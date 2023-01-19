S = input()
arr = []
for i in range(len(S)-1,-1,-1):
    arr.append(S[i:])
arr.sort()
for i in arr:
    print(i)