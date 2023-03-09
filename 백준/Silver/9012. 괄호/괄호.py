#basecase - 문자열의 마지막 문자를 확인할 때
#cnt 가 1이 아니면 no를 return 해야 함
#1이면 yes

def find_VPS(word,cnt):
    if cnt == 0 and (len(word)%2 == 1 or word[-1] == '(') or cnt < 0:
        return "NO"
    elif len(word) == 1:
        if cnt != 1:
            return "NO"
        else:
            return "YES"
    else:
        if word[0] == '(':
            # find_VPS(find_VPS(word[1:],cnt+1))
            #이렇게 하면 괄호가 끝나도 그 다음 인자를 확인할 수 있다.
            #하지만 괄호가 계속 된다면?
            return find_VPS(word[1:],cnt+1)
        else:
            return find_VPS(word[1:],cnt-1)


T = int(input())

for _ in range(T):
    word = input()
    print(find_VPS(word,0))
