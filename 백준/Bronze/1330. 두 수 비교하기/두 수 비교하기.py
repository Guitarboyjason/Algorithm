a,b = input().split()
result = int(a)-int(b)
if result > 0:
    print(">")
elif result == 0:
    print("==")
else :
    print("<")