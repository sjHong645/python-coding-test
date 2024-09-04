import sys
sys.setrecursionlimit(10000)

input = sys.stdin.readline

# 노드개수 n, 엣지개수 m
n, m = map(int, input().split())

A = [[] for _ in range(n+1)] # 인접 리스트로 구현한 그래프 

visited = [False] * (n+1) # 방문 리스트 

def DFS(v) : 
    visited[v] = True

    for neighbor in A[v] : 
        if visited[v] == False : 
            DFS(neighbor)

for _ in range(m) : 

    start, end = map(int, input().split())

    A[start].append(end)
    A[end].append(start)

count = 0

for i in range(1, n+1) : 
    if visited[i] == False : 
        count += 1
        DFS(i)

print(count)