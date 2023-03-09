import string
from collections import deque
hansoo_name = input()

letter_dict = {i : 0 for i in string.ascii_uppercase}

for letter in hansoo_name:
    letter_dict[letter] += 1

# for i in letter_dict.values():
if sum([1 for i in letter_dict.values() if i % 2 == 1]) > 1:
    print("I'm Sorry Hansoo")
else:
    middle = [i[0] for i in letter_dict.items() if i[1]%2 == 1]
    answer=""
    if middle:
        answer = middle[0]
        letter_dict[middle[0]] -= 1
    first = ""
    # for i in range(len(hansoo_name)):
    tmp = deque([[i[0]]*int(i[1]//2) for i in letter_dict.items() if i[1] > 0])
    # print(tmp)
    while tmp:
        first+="".join(tmp.popleft())
    answer = first+answer+first[::-1]
    print(answer)
        
        
