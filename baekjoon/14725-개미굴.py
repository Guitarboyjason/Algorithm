###### 출력하는 함수 #######

def food_printer(dict_foods,layer):
    list_foods = sorted(list(dict_foods))		# 사전순으로 접근해야 하므로 dict_foods의 key들을 리스트로 만들어 정렬
    for i in list_foods:
        print("--"*layer,end="")
        print(i)
        food_printer(dict_foods[i],layer+1)		# 재귀 형식으로 재접근


###### 입력과 데이터 처리 ######
N = int(input())
dict_foods = dict()
for i in range(N):
    K,*foods = input().split()		#처음 들어오는 수를 제외한 나머지가 음식들

    layer = dict_foods		#계속해서 내려가야 하기 때문에 tmp에 해당 dictionary를 부여하여 접근할 수 있도록 함
    for food in foods:	#들어온 음식의 순서대로 확인
        if food not in layer:	# 존재하지 않는다는 뜻이기 때문에 해당 음식을 key로 하여 새로운 dictionary 생성
            layer[food] = dict()	
        layer = layer[food]		#다음 층으로 진행
print(dict_foods)
food_printer(dict_foods,0)
