N = int(input())
dict_foods = dict()
for i in range(N):
    K,*foods = input().split()
    K = int(K)
    # arr_foods.append(foods)
    # for food in foods:
    tmp = dict_foods
    # food = foods[0]
    for food in foods:
        # print(food)
        if food in tmp:
            tmp = tmp[food]
            continue
        tmp[food] = dict()
        tmp = tmp[food]
    # while food in tmp:
    #     tmp = tmp[food]
    # # if food not in dict_foods:
    # tmp[food] = dict()
    # print(tmp)
    # print(dict_foods)
# dict_foods.sort()
# print(arr_foods)
# print(*dict_foods)
# for i in dict_foods:
# print(list(dict_foods))
# dict_foods = list(dict_foods)


# for foods in dict_foods:
def food_printer(dict_foods,layer):
    list_foods = sorted(list(dict_foods))
    for i in list_foods:
        print("--"*layer,end="")
        print(i)
        food_printer(dict_foods[i],layer+1)

food_printer(dict_foods,0)