words= input()
for word in words:
    if "A"<=word<"N" or "a"<=word<"n":
        word = chr(ord(word)+13)
    elif "N"<=word<="Z" or "n"<=word<="z":
        word = chr(ord(word)-13)
    print(word,end="")