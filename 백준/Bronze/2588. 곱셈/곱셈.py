n1=input()
n2=input()

tmp = int(n2)
while tmp/10 != 0:
    print(int(n1)*(tmp%10))
    tmp //=10
print(int(n1)*int(n2))