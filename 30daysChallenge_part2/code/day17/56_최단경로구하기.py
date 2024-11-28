import sys
from queue import PriorityQueue

V, E = map(int, input().split()) # 노드 개수, 엣지 개수 
K = int(input()) # 출발 노드 번호 

distance = [sys.maxsize] * (V+1)
visited = [False] * (V+1)
myList = [[] for _ in range(V+1)]

q = PriorityQueue()

for _ in range(E) : 
    u, v, w = map(int, input().split())
    myList[u].append(v, w)

q.put((0, K)) # K번째 노드는 시작 노드이기 때문에 최단 거리는 0
distance[K] = 0

while q.qsize() > 0 : 
    current = q.get() # 가중치가 가장 작은 (최단 거리, 노드 번호)
    
    current_v = current[1] # 노드 번호 

    # 현재 노드를 방문한 적이 있다면 넘어간다
    if visited[current_v] : 
        continue 

    visited[current_v] = True 

    # 현재 노드와 이웃한 노드를 탐색 
    for nb in myList[current_v] : 
        
        next = nb[0] # 이웃한 노드 
        weight = nb[1] # 이웃한 노드와의 가중치 

        # 이웃한 노드의 최단 거리가 
        # 현재 노드 + 엣지 가중치보다 크다면 

        # 작은 값으로 업데이트
        if distance[next] > distance[current_v] + weight : 
            distance[next] = distance[current_v] + weight 

            q.put((distance[next], next)) # (최단 거리, 노드 번호)를 큐에 삽입

for i in range(1, V+1) : 

    if visited[i] : 
        print(distance[i])

    else :
        print("INF")