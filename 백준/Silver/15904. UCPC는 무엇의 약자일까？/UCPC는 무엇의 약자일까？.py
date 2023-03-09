
line = input()
compare = "UCPC"
for i in line:
    if i == compare[0]:
        if len(compare) == 1:
            compare = ""
            print("I love UCPC")
            break
        compare = compare[1:]
if len(compare):
    print("I hate UCPC")
