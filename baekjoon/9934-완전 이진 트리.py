K = int(input())
buildings= list(map(int,input().split()))
# 가장 아래를 제외한 모든 노드는 왼쪽과 오른쪽 자식을 갖고 있다

# 그러면 반을 쪼개어 레이어에 추가하면 될 것

# while buildings:

def graph_controller(graph):
    if len(graph) == 1:
        return graph[0]
    answer = []
    middle = len(graph)//2
    # answer.append([graph[len(graph)//2]])
    # answer.append(graph[middle])
    answer.append([graph_controller(graph[:middle])])
    answer.append([graph_controller(graph[middle +1:])])
    print(graph[middle])
    print(graph_controller(graph[:middle  ])) 
    print(graph_controller(graph[middle+1:]))
    return answer

print(graph_controller(buildings))