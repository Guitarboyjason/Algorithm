def isPalindrom(string):
    return recursion(string,0,len(string)-1,1)
def recursion(string,start,end,count):
    if(start>=end):
        return 1,count
    elif string[start] != string[end] :
        return 0,count
    else:
        return recursion(string,start+1,end-1,count+1)
T = int(input())
for test_case in range(T):
    string = input()
    print(f"{isPalindrom(string)[0]} {isPalindrom(string)[1]}")
