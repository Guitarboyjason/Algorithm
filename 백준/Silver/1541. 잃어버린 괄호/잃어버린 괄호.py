# 괄호를 적절히 쳐서 이 식의 값을 최소로 만드려 한다.
# 값을 최소로 만드는 프로그램을 작성하라

# 곱셈과 덧셈이 없으므로 음수를 기준으로 생각하면 될 것 같다.
# 뺄셈 뒤에 덧셈이 길게 들어올 수 있도록

formula = input()

flag = False
operations = ["+","-"]
answer_formula = ""
# answer = 0
num = ""
for c in formula:
    if c in operations:
        answer_formula += str(int(num))
        num = ""
        if c == "-":
            if flag:
                answer_formula+=")" + c +"("
            else:
                answer_formula+=c + "("
            flag = True
        else:
            answer_formula += c
    else:
        num += c
answer_formula += str(int(num))
if flag:
    answer_formula += ")"
print(eval(answer_formula))