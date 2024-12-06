N = int(input())
visited = [False] * (N)
tree = [[] for _ in range(N)]
answer = 0
p = list(map(int, input().split())) 

# 트리 데이터 저장
for i in range(N) : 
    
    if p[i] != -1 : 
        tree[i].append(p[i])
        tree[p[i]].append(i)
        
    else : 
        root = i

# DFS 탐색 메소드
def DFS(number) : 
    
    global answer 
    visited[number] = True 
    child_node = 0
    
    for i in tree[number] : 
        
        # 아직 방문하지 않았고 삭제 대상 노드가 아닐 경우에만 
        # 자식노드에 대한 탐색 지속
        if not visited[i] and i != deleteNode : 
            child_node += 1
            DFS(i)
            
    if child_node == 0 :
        answer += 1 

deleteNode = int(input())

if deleteNode == root : # 루트노드가 삭제될 경우
    print(0)
    
else :
    DFS(root)
    print(answer)