A = input()
operator = input()
B = input()

if operator == "+":
    print(int(A)+int(B))
else:
    print(10**(len(A)+len(B)-2))
