import sys

word = sys.stdin.readline().rstrip()
M = int(sys.stdin.readline().rstrip())
left = list(word)
rev_right = []
for _ in range(M):
    command = sys.stdin.readline().rstrip()
    if command == 'L':
        if len(left) > 0:
            rev_right.append(left.pop())
    elif command == 'D':
        if len(rev_right) > 0:
            left.append(rev_right.pop())
    elif command == "B":
        if len(left) > 0:
            left.pop()
    else:
        P,letter = command.split()
        left.append(letter)
print("".join(left+list(reversed(rev_right))))
