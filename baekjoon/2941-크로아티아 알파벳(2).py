croatia = ['c=','c-','dz=','d-','lj','nj','s=','z=']
word = input()
count = 0
while word != "":
    if len(word) >= 2:
        if word[:2] in {'c=','c-','d-','lj','nj','s=','z='}:
            word = word[2:]
        elif word[:3] == 'dz=':
            word = word[3:]
        else:
            word = word[1:]
    else:
        word = ""
    count += 1
print(count)
