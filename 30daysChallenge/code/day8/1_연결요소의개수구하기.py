# https://www.acmicpc.net/problem/11724

import sys

input = sys.stdin.readline
n, m = map(int, input().split())

A = [[] for _ in range(n+1)]
visited = [False] * (n+1)

def DFS(v) : 
    visited[v] = True
    
    for i in A[v] : 
        if not visited[v] : 
            DFS(i)
            
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