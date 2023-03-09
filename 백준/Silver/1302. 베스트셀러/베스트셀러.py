N = int(input())
titles = [input()for _ in range(N)]
titles.sort()
print(max(titles,key=lambda x : titles.count(x)))