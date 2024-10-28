from collections import deque

N, M, start = map(int, input().split())

A = [[] for _ in range(N+1)]

for _ in range(M) : 
    s, e = map(int, input().split())

    A[s].append(e) # 양방향 edge 그래프라서 양쪽에서 노드를 추가한다
    A[e].append(s)

# 번호가 작은 노드부터 방문하도록 하기 위해서 정렬 
for i in range(N+1) : 
    A[i].sort()

def DFS(v) : 
    print(v, end = ' ')
    visited[v] = True

    for i in A[v] :
        if not visited[i] : 
            DFS(i)

visited = [False] * (N + 1)
DFS(start)

def BFS(v) :

    queue = deque()
    queue.append(v)
    visited[v] = True 

    while queue : 

        now_node = queue.pop()
        print(now_node, end = ' ')

        for neighbor in A[now_node] : 

            if visited[neighbor] == False : 
                visited[neighbor] = True
                queue.append(neighbor)
print()
visited = [False] * (N + 1)
BFS(start)