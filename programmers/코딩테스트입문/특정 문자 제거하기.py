import re

mystring = "afbcdef"
letter = "f"

p = re.compile(letter)

m = p.finditer(mystring)

print(mystring.replace(letter,""))


print([i for i in mystring if i != letter])
answer = ""
for i in [i for i in mystring if i != letter]:
    answer += i


print([i for i in list(m)])
