number_filter = [str(i) for i in range(10) if i != 4 and i != 7]
N = int(input())

for number in range(N,3,-1):
    num_list = [1 for i in str(number) if i in number_filter]
    if len(num_list) == 0:
        print(number)
        break
    
    