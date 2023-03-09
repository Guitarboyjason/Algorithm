balls = ["big","","","small"]
def A() :
    tmp = balls[0]
    balls[0] = balls[1]
    balls[1] = tmp

def B() :
    tmp = balls[0]
    balls[0] = balls[2]
    balls[2] = tmp

def C():
    tmp = balls[0]
    balls[0] = balls[3]
    balls[3] = tmp

def D():
    tmp = balls[1]
    balls[1] = balls[2]
    balls[2] = tmp

def E():
    tmp = balls[1]
    balls[1] = balls[3]
    balls[3] = tmp

def F():
    tmp = balls[2]
    balls[2] = balls[3]
    balls[3] = tmp

suffle = input()
for i in suffle:
    if i == "A":
        A()
    elif i == "B":
        B()
    elif i == "C":
        C()
    elif i == "D":
        D()
    elif i == "E":
        E()
    else:
        F()
print(balls.index("big")+1)
print(balls.index("small")+1)
