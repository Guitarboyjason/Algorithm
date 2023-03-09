import math
color_arr = ["black","brown","red","orange","yellow"\
    ,"green","blue","violet","grey","white"]

first = input()
second = input()
color = input()

print((color_arr.index(first)*10 + color_arr.index(second))*int(math.pow(10,color_arr.index(color))))