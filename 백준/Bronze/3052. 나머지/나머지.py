n = 10
arr = set()
for cnt in range(n):
    a = int(input())
    arr.add(a%42)
print(len(arr))