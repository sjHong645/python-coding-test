N = int(input())
tree = {}

for _ in range(N) : 
    root, left, right = input().split()
    
    tree[root] = [left, right]
    
def preOrder(now) : 
    
    if now == '.' : 
        return 
    
    print(now, end = '') # 현재 노드 
    print(tree[now][0])  # 왼쪽 노드 
    print(tree[now][1])  # 오른쪽 노드
    
def inOrder(now) : 
    
    if now == '.' : 
        return 
    
    print(tree[now][0])  # 왼쪽 노드 
    print(now, end = '') # 현재 노드 
    print(tree[now][1])  # 오른쪽 노드
    
def postOrder(now) : 
    
    if now == '.' : 
        return 
        
    print(tree[now][0])  # 왼쪽 노드 
    print(tree[now][1])  # 오른쪽 노드
    print(now, end = '') # 현재 노드 

preOrder('A')
print()
inOrder('A')
print()
postOrder('A')