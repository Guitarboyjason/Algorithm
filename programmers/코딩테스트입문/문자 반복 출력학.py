def solution(my_string,n):
    answer = "".join(i*n for i in my_string)

    return answer

my_string = "hello"
n = 3

print(solution(my_string,n))
