def isPalindrome(s):
    global n
    n = 1
    return recursion(s, 0, len(s)-1)


def recursion(s, l, r):
    global n
    if l >= r:
        return 1
    elif s[l] != s[r]:
        return 0
    else:
        n += 1
        return recursion(s, l+1, r-1)


n = 1

a = int(input())
for i in range(a):
    s = input()
    print(isPalindrome(s), n)
