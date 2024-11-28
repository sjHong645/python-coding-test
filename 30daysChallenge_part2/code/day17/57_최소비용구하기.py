import sys
from queue import PriorityQueue

N = int(input())
M = int(input())

myList = [[] for _ in range(N+1)]
distance = [sys.maxsize] * (N+1)
visited = [False] * (N+1)

for _ in range(M) : 
    start, end, weight = map(int, input().split())
    myList[start].append((end, weight)) # (목적지 노드, 가중치) 
    
start_index, end_index = map(int, input().split())

def dijkstra(start, end) : 
    
    pq = PriorityQueue()
    pq.put((0, start)) # (최단 거리, 노드) 
                       # 이래야 거리가 가장 짧은 데이터가 먼저 pop될 수 있다
    
    distance[start] = 0
    
    while pq.qsize() > 0 : 
        now = pq.get()
        now_node_number = now[1]
        
        if not visited[now_node_number] : 
            
            visited[now_node_number] = True
            
            for n in myList[now_node_number] : 
                
                if not visited[n[0]] and distance[n[0]] > distance[now_node_number] + n[1] : 
                    distance[n[0]] = distance[now_node_number] + n[1]
                    pq.put((distance[n[0]], n[0])) # 우선순위 큐에 넣을 데이터 
                                                   # (최단 거리, 노드) 
                                                   
    return distance[end]

print(dijkstra(start_index, end_index))
    
    