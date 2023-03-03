#괄호를 적절하게 쳐서 식 값의 최솟값을 만들자

line = input()
tmp_line = line.replace('+','-')
arr_num = [int(i) for i in tmp_line.split(sep='-')]
arr_oper = []
for i in line:
    if i == '-' or i == '+':
        arr_oper.append(i)
# print(arr_num)
# print(arr_oper)
# print(line)
index = -1
for i in range(len(arr_oper)):
    if arr_oper[i] == '-':
        index = i
        break
sum = 0
if index != -1:
    for i in range(index+1):
        sum += arr_num[i]
    for i in range(index+1,len(arr_num)):
        sum -= arr_num[i]
else:
    for i in range(len(arr_num)):
        sum += arr_num[i]
print(sum)
