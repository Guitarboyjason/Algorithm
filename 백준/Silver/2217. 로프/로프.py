N = int(input())
rope = []
for _ in range(N):
    rope.append(int(input()))

#병렬에 참가하는 로프중 최소의 로프 * 참가하는 로프의 수 가 결과
#병렬에 참가할 때와 참가하지 않을때 어떤게 더 많은 중량을 들 수 있는지 비교

rope.sort()
max = 0
for i in range(len(rope)):
    if max < (len(rope) - i) * rope[i]:
        max = (len(rope) - i) * rope[i]
print(max)
