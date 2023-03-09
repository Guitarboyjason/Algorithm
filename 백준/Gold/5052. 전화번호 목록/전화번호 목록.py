import sys
class Node(object):
    def __init__(self,key,data = None):
        self.key = key
        self.data = data
        self.children = {}

class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self,string):
        current_node = self.head
        for char in string:
            if char not in current_node.children:
                current_node.children[char] = Node(char)
            current_node = current_node.children[char]    
        current_node.data = string ##done_flag
        
    def search(self,string):
        current_node = self.head
        for char in string:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]
        if current_node.data:
            return True
        return False
    
    def starts_with(self,prefix):
        current_node = self.head
        words = []
        for p in prefix:
            if p not in current_node.children:
                return False
            current_node = current_node.children[p]
        
        current_node = [current_node]    
        next_node = []
        
        while True:
            for node in current_node:
                if node.data:
                    words.append(node.data)
                next_node.extend(list(node.children.values()))
            if len(next_node) != 0:
                current_node = next_node
                next_node = []
            else:
                break
        return words

for t in range(int(sys.stdin.readline())):    
    trie = Trie()
    n = int(sys.stdin.readline())
    nums = [sys.stdin.readline().rstrip() for _ in range(n)]
    for num in nums:
        trie.insert(num)
    
    for num in nums:
        if len(trie.starts_with(num)) > 1:
            print("NO")
            break
    else:
        print("YES")
