#이진 트리를 입력받아 전위 순회(preorder traversal),
#중위 순회(inorder traversal),
# 후위 순회(postorder traversal)한 결과를 출력

#전위 : preorder - 부모노드 먼저, 왼쪽,오른쪽 자식 순
#중위 : inorder - 왼쪽, 부모, 오른쪽 순
#후위 : postorder - 왼쪽, 오른쪽, 부모 순

def find_root(nodes):
    root = []
    for i in nodes:
        root.append(i[0])
    for i in nodes:
        if i[1] in root:
            root.remove(i[1])
        if i[2] in root:
            root.remove(i[2])
    return root[0]

def find_index(nodes, node):
    for i in range(len(nodes)):
        if nodes[i][0] == node:
            return i
    return -1

def preorder(nodes,root):
    if root == -1:
        return 0
    print(nodes[root][0], end='')
    preorder(nodes,find_index(nodes,nodes[root][1]))
    preorder(nodes,find_index(nodes,nodes[root][2]))

def inorder(nodes,root):
    if root == -1:
            return 0
    inorder(nodes,find_index(nodes,nodes[root][1]))
    print(nodes[root][0], end='')
    inorder(nodes,find_index(nodes,nodes[root][2]))

def postorder(nodes,root):
    if root == -1:
        return 0
    postorder(nodes,find_index(nodes,nodes[root][1]))
    postorder(nodes,find_index(nodes,nodes[root][2]))
    print(nodes[root][0], end='')


N = int(input())
nodes = []
for _ in range(N):
    root, left, right = input().split()
    nodes.append([root,left,right])

root = find_root(nodes)

root = find_index(nodes,root)
preorder(nodes, root)
print()
inorder(nodes,root)
print()
postorder(nodes,root)
