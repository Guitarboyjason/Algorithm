N = int(input())

pattern = input()
# pattern_before = []

for i in range(len(pattern)):
    if pattern[i] == '*':
        pattern_before = pattern[:i]
        pattern_after = pattern[i+1:]

# before = True
# for i in pattern:
#     if i == '*':
#         before = False
#     if before:
#         pattern_before.append(i)
# pattern_before = ''.join(pattern_before)

arr = []
for i in range(N):
    arr.append(input())

for i in arr:
    if len(i) >= len(pattern)-1:
        if i[:len(pattern_before)] == pattern_before and i[-len(pattern_after):] == pattern_after:
            print("DA")
        else:
            print("NE")
    else:
        print("NE")
