# # 1000글자까지이므로 N**2까지는 가능 할 것.


# # dp로 접근을 해야할 것 같다.
# # 해당 문자를 포함을 하든 안하든 있는지를 확인한ㄴ다....?
# # 이러면 문제가 생기는게 어느 인덱스까지 확인을 했는지 알 수 없다.
# # 그럼 해당 문자를 포함할 때 -> 앞의 배열들로 만들어진 수열 중
# # 가장 길이가 긴 것 -> 확인한 인덱스가 가장 작은것 순으로 확인..?


# # 배열에서 앞에 나온 문자들을 포함 하든 안하든 결국 최댓값은 정해져있다.....
# # 
# word_1 = input()
# word_2 = input()

word_1 = input()
word_2 = input()

cnt_list = [[0 for i in range(len(word_1)+1)]for j in range(len(word_2)+1)]
# print(cnt_list)

for i in range(1,len(word_2)+1):
    for j in range(1,len(word_1)+1):
        if word_2[i-1] == word_1[j-1]:
            cnt_list[i][j] = cnt_list[i-1][j-1]+1
        else:
            cnt_list[i][j] = max(cnt_list[i][j-1],cnt_list[i-1][j])
print(cnt_list[-1][-1])