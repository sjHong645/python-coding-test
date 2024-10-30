from collections import deque

N, M, Start = map(int, input().split())

A = [[] for _ in range(N+1)]

for _ in range(M) : 
    
    start, end = map(int, input().split())
    A[start].append(end)
    A[end].append(start)
    
for i in range(N+1) : 
    A[i].sort()
    
visited = [False] * (N+1)
def DFS(n) : 
    
    print(n, end = ' ')
    visited[n] = True 
    
    for nb in A[n] : 
        if not visited[nb] : 
            DFS(nb)

DFS(Start)

visited = [False] * (N+1)

def BFS(start) : 
    
    queue = deque()
    queue.append(start)
    
    visited[start] = True
    
    while len(queue) != 0 : 
        
        node = queue.popleft()
        
        for i in A[node] : 
            if not visited[i] : 
                visited[i] = True
                queue.append(i)
                
BFS(Start)