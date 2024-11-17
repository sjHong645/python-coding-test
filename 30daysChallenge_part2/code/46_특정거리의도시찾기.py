from collections import deque

N, M, K, X = map(int, input().split())

A = [[] for _ in range(N+1)]
answer = []
visited = [-1] * (N+1) # 방문하지 않았다면 -1 
                       # 방문했다면 0이상의 값 
                       # 이때, 저장된 값은 특정 시작 노드에서의 최단 거리값 

def BFS(v) : # v라는 노드에서 시작 
    queue = deque() 
    queue.append(v)

    visited[v] += 1

    while queue : 

        now_Node = queue.popleft() 

        for i in A[now_Node] : 
            if visited[i] == -1 : 
                visited[i] = visited[now_Node] + 1 
                queue.append(i)

for _ in range(M) : 
    S, E = map(int, input().split()) # 시작점, 도착점
    A[S].append(E)

BFS(X)

for i in range(N+1) : 
    if visited[i] == K : 
        answer.append(i)

if not answer : 
    print(-1)

else :
    answer.sort()
    for i in answer : 
        print(i)
