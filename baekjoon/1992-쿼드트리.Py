import sys
sys.setrecursionlimit = 10**10


def quad(graph):
    if "1" not in "".join(graph):
        return "0"
    elif "0" not in "".join(graph):
        return "1"
    else:
        return "("+str(quad(graph[:len(graph)//2][:len(graph)//2])) + ")" + "("+str(quad(graph[:len(graph)//2][len(graph)//2:])) + ")" + "("+str(quad(graph[len(graph)//2:][:len(graph)//2])) + ")" + "("+str(quad(graph[len(graph)//2:][len(graph)//2:])) + ")"


N = int(input())
graph = [list(input()) for _ in range(N)]
print(graph)
print(graph[:len(graph)//2][:len(graph)//2])
# print(quad(graph))
# print("1" not in "".join(["1"]))
