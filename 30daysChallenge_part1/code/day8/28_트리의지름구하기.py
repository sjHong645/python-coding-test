from collections import deque

N = int(input())
A = [[] for _ in range(N)]

# 그래프 데이터 삽입
for _ in range(N) : 
    
    Data = list(map(int, input().split()))
    
    index = 0
    
    S = Data[index] # 정점 
    index += 1
    
    while True : 
        E = Data[index] # 이웃노드 
        
        if E == -1 : 
            break
        
        V = Data[index + 1] # 가중치 
        
        A[S].append((E, V))
        
        index += 2 
        
distance = [0] * (N+1)
visited = [False] * (N+1)

def BFS(v) : 
    
    queue = deque() 
    queue.append(v) # 큐에는 노드의 순번만 넣는다. 
                    # 가중치 데이터까지는 넣지 않는다. 
                    # 왜냐하면, 모든 노드에 방문했는지를 따지는 것이기 때문에 가중치 데이터까지는 필요없다.
    visited[v] = True 
    
    while queue : 
        
        now_Node = queue.popleft()
        
        for i in A[now_Node] : 
            
            if not visited[i[0]] : 
                
                visited[i[0]] = True
                queue.append(i[0])
                distance[i[0]] = distance[now_Node] + i[1]

BFS(1)
Max = 1

# 임의의 노드에서 가장 거리가 먼 노드 찾기 
for i in range(2, N+1) : 
    if distance[Max] < distance[i] : 
        Max = i
        
# 다시 초기화
distance = [0] * (N+1)
visited = [False] * (N+1)

# 임의의 노드에서 가장 거리가 먼 노드에서 다시 시작
BFS(Max) 

# distance의 최댓값 출력
distance.sort()
print(distance[N])
