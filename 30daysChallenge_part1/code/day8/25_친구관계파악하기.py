import sys

input = sys.stdin.readline

N, M = map(int, input().split())
arrive = False

A = [[] for _ in range(N+1)]
visited = [False] * (N+1)

for _ in range(M) : 
    
    start, end = map(int, input().split())
    
    A[start].append(end)
    A[end].append(start)
        

def DFS(n, depth) : 
    
    global arrive
    
    if depth == 5 : 
        arrive = True
        return

    # depth 단계의 현재 노드 방문 표시 
    visited[n] = True
    
    # depth+1 단계의 노드를 DFS를 통해 방문 
    for nb in A[n] : 
        
        if not visited[nb] : 
            DFS(nb, depth + 1)
            
    # depth 단계의 다른 노드에서 visited를 사용하기 위해서 원상복구
    visited[n] = False
            
for i in range(N) : 
    DFS(i, 1)
    
    if arrive : 
        break
    
if arrive : 
    print(1)
    
else : 
    print(0)