N,B = input().split()
B = int(B)
change_dict = {chr(i+55) : i for i in range(10,36)}
summary = 0
for idx, char in enumerate(reversed(N)):
    if char in change_dict:
        summary += B**idx * change_dict[char]
    else:
        summary += B**idx * int(char)
print(summary)