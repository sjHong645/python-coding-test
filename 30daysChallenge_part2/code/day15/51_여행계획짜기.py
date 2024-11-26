N = int(input())
M = int(input())
city = [[0 for j in range(N+1)] for i in range(N+1)]

parent = [0] * (N+1)

def find(a) : 
    if a == parent[a] : 
        return a 
    
    else :
        parent[a] = find(parent[a])
        return parent[a]
    
def union(a, b) : 
    a = find(a)
    b = find(b)
    
    if a != b : 
        parent[b] = a
        
for i in range(1, N+1) : 
    city[i] = list(map(int, input().split()))    
    city[i].insert(0, 0) # 0번째 행은 빈 공간이라서 그걸 채워넣기 위한 코드
    
route = list(map(int, input().split()))
route.insert(0, 0) # 마찬가지 

for i in range(1, N+1) : 
    parent[i] = i
    
for i in range(1, N+1) : 
    for j in range(1, N+1) : 
        if city[i][j] == 1 : 
            union(i, j)
            
isConnect = True 
index = find(route[1]) # 모든 도시가 하나의 집합에 속해 있는지를 따질려고 한다.
                       # 그래서 여행 계획에 속한 도시 중 
                       # 가장 앞에 있는 도시를 대표 도시로 지정했다

for i in range(2, len(route)) : 
    if index != find(route[i]) : # 도시계획에 속한 도시 중 단 하나라도 
                                 # 다른 집합에 속해있다면 여행 계획이 수립될 수 없다
        isConnect = False
        break
    
if isConnect : 
    print("YES")
    
else : 
    print("NO")