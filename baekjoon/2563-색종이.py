drawing_paper = [[False for _ in range(100)]for _ in range(100)]
n = int(input())
papers = [list(map(int,input().split()))for _ in range(n)]

for paper in papers:
    for x in range(paper[0],paper[0]+10):
        for y in range(paper[1],paper[1]+10):
            drawing_paper[x][y] = True
            
print(sum(i.count(True) for i in drawing_paper))