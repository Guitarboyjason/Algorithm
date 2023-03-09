

time = 0
now = "A"

line = input()
for i in line:
    time += min(abs(ord(now)-ord(i)), 26-abs(ord(now)-ord(i)))
    now = i
print(time)
