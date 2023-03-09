import sys
# sys.stdin = open("input.txt","r")
guess = int(input())
ollie = [False]+ [True for _ in range(10)]
lier = False
answer = {i : "" for i in range(1,11)}
while guess:
    stan = input()
    if stan == "right on":
        if ollie[guess] == False:
            lier = True
        if lier:
            print("Stan is dishonest")
        else:
            print("Stan may be honest")
        ollie = [False]+[True for _ in range(10)]
        answer = {i : "" for i in range(1,11)}
        
        lier = False
    elif stan == "too high":
        for i in range(guess,11):
            if answer[i] == "too low":
                lier = True
            answer[i] = "too high"
        answer[guess] = stan
        ollie[guess:] = [False]*len(ollie[guess:])
    else:
        for i in range(1,guess+1):
            if answer[i] == "too high":
                lier = True
            answer[i] = "too low"
        ollie[:guess+1] = [False]*len(ollie[:guess+1])
    # print(ollie)
    # if True not in ollie:
    #     lier = True
    guess = int(input())

