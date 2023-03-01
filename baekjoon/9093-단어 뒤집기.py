for _ in range(int(input())):
    sentence = list(input().split())
    for i in sentence:
        print(i[::-1],end=" ")
    print()