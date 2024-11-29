import sys

N, M = map(int, input().split())
edges = []
distance = [sys.maxsize] * (N+1)

for i in range(M) : 
    start, end, weight = map(int, input().split())
    edges.append((start, end, weight))
    
# 벨만 포드 수행 
distance[1] = 0 # 시작 노드인 1의 거리 리스트 값을 0으로 초기화

for _ in range(N-1) : 
    
    for start, end, weight in edges : 
        
        if distance[start] != sys.maxsize and distance[end] > distance[start] + weight : 
            distance[end] = distance[start] + weight
            
# 음수 사이클 존재 여부 확인
cycle_flag = False

for start, end, weight in edges : 
        
    if distance[start] != sys.maxsize and distance[end] > distance[start] + weight : 
        cycle_flag = True
        
if not cycle_flag : 
    for i in range(2, N+1) : 
        if distance[i] != sys.maxsize : 
            print(distance[i])
            
        else :
            print(-1)

else : 
    print(-1)