sang = int(input())
joong = int(input())
ha = int(input())
coke = int(input())
cider = int(input())

min_burger = min(sang,joong,ha)
min_drink = min(coke,cider)
print(min_burger+min_drink-50)