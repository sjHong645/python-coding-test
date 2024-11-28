import sys
import heapq

N, M, K = map(int, input().split())
W = [[] for _ in range(N+1)]

distance = [[sys.maxsize] * K for _ in range(N+1)]

for _ in range(M) : 
    a, b, c = map(int, input().split())
    W[a].append((b, c))

pq = [(0, 1)] # 가중치를 우선으로 정렬해야 해서 (가중치, 노드) 순으로 저장한다
distance[1][0] = 0 

while pq : 
    cost, node = heapq.heappop(pq)

    for nNode, nCost in W[node] : 
        sCost = cost + nCost
        
        if distance[nNode][K-1] > sCost : 

            distance[nNode][K-1] = sCost
            distance[nNode].sort()
            heapq.heappush(pq, [sCost, nNode])

for i in range(1, N+1) : 
    if distance[i][K-1] == sys.maxsize : 
        print(-1)
    else : 
        distance[i][K-1]