for test_case in range(int(input())):
    L = list(input().split())
    print("Case #{}: ".format(test_case+1), end="")
    for i in L[::-1]:
        print(i, end=" ")
    print()
