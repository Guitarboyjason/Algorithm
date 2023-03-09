# def triangle(dot1,dot2,dot3):
#     #길이 구하기
#     a = ((dot1[0]-dot2[0])**2 + (dot1[1]-dot2[1])**2)**0.5
#     b = ((dot2[0]-dot3[0])**2 + (dot2[1]-dot3[1])**2)**0.5
#     c = ((dot3[0]-dot1[0])**2 + (dot3[1]-dot1[1])**2)**0.5
#     # print(a,b,c)
#     if not a or not b or not c:
#         return 0
#     #코사인 값 구하기 (코사인 제 2법칙)
#     cos = (a**2+b**2-c**2)/(2*a*b)
#     #사인 값 구하기 (cos**2 + sin**2 == 1)
#     sin = (1-cos**2)**0.5
#     #높이 구하기
#     h = sin*a
#     #결과 반환
#     return 1/2*b*h

# N = int(input())
# dots = [list(map(int,input().split())) for _ in range(N)]
# middle = [sum([i[0] for i in dots])/N,sum([i[1] for i in dots])/N]
# # 중심점
# dots.append(dots[0])

# answer = 0
# for i in range(N):
#     a = dots[i]
#     b = dots[i+1]
#     c = middle
    
#     answer += triangle(a,b,c)
    
# print(round(answer,2))

N = int(input())
dots = [list(map(int,input().split()))for _ in range(N)]
dots.append(dots[0])
answer = 0
for i in range(N):
    answer+= dots[i][0] * dots[i+1][1]
    answer -= dots[i+1][0] * dots[i][1]
print(round(abs(answer/2),2))