word = input().upper()

arr = [0]*26
for i in word:
    arr[ord(i)-65] += 1
if arr.count(max(arr))>1:
    print("?")
else:
    print(chr(arr.index(max(arr)) + 65))
