from collections import deque

N, M = map(int, input().split())
A = [[] for _ in range(N+1)] 
answer = [0] * (N+1)

def BFS(v) : 
    queue = deque()
    queue.append(v)
    visited[v] = True

    while queue : 
        now_Node = queue.popleft()
        for i in A[now_Node] : 
            if not visited[i] : 
                visited[i] = True 
                answer[i] += 1 # now_Node -> i 노드로 방문할 수 있다는 건
                               # i노드가 now_Node의 신뢰를 받고 있다는 뜻 
                queue.append(i) 

for _ in range(N) : 
    S, E = map(int, input().split())
    A[S].append(E)

for i in range(1, N+1) : 
    visited = [False] * (N+1)
    BFS(i)

maxVal = 0

for i in range(1, N+1) : 
    maxVal = max(maxVal, answer[i])

for i in range(1, N+1) : 
    if maxVal == answer[i] : 
        print(i, end = ' ')