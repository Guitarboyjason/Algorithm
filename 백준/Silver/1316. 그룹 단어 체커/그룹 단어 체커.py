n = int(input())

def groupWordChecker(word):
    
    checker = []
    if len(word) == 1 or len(word) == 2:
        return 1
    else:
        for i in range(len(word)-1):
            if word[i]!= word[i+1]:
                if word[i+1] in checker:
                    return 0
                else:
                    checker.append(word[i])
            if i == len(word)-2:
                return 1

sum = 0
for _ in range(n):
    word = input()
    sum += groupWordChecker(word)
print(sum)
