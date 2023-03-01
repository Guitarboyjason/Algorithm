for test_case in range(1,int(input())+1):
    lines = list(map(int,input().split()))
    lines.sort()
    print("Scenario #{}:".format(test_case))
    if lines[-1]**2 == lines[0]**2 + lines[1]**2:
        print("yes")
    else:
        print("no")
    print()