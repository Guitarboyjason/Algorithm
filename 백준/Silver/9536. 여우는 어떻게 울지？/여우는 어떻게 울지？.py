
T = int(input())
for _ in range(T):
    sounds = input().split()
    animals = input()
    while animals != "what does the fox say?":
        animals = animals.split(" goes ")
        while animals[1] in sounds:
            sounds.pop(sounds.index(animals[1]))
        animals = input()
    print(" ".join(sounds))


