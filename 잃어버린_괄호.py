# 괄호를 적절히 쳐서 이 식의 값을 최소로 만드려 한다.
# 값을 최소로 만드는 프로그램을 작성하라

# 곱셈과 덧셈이 없으므로 음수를 기준으로 생각하면 될 것 같다.
# 뺄셈 뒤에 덧셈이 길게 들어올 수 있도록

formula = input()

flag = False # 뺄셈이 나왔었는지에 대한 flag
operations = ["+","-"]
answer_formula = ""
num = "" # 숫자를 int형으로 바꾸고 다시 str으로 더해주기 위한 변수
for c in formula:
    if c in operations:
        answer_formula += str(int(num)) # 식에 num을 더한다.
        num = "" # num 초기화
        if c == "-": # 뺄셈이 들어옴
            if flag: # 이전에 뺄셈이 들어온 적 있음
                answer_formula+=")" + c +"(" # 닫았다가 다시 뺄셈
            else: # 첫 뺄셈
                answer_formula+=c + "(" #열어준다.
            flag = True
        else: # 덧셈
            answer_formula += c
    else: # 숫자
        num += c
answer_formula += str(int(num)) # 마지막에 남아있던 숫자
if flag: # 뺄셈이 들어온 적 있으면
    answer_formula += ")" # 닫아준다.
print(eval(answer_formula)) # 계산