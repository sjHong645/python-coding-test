
N, M = map(int, input().split())
parent = [0] * (N+1)

def find(a) : 
    if a == parent[a] : # a가 대표노드이면 그대로 반환 
        return a
    
    else : # 그렇지 않다면 대표노드를 찾아서 변경하고 
           # 반환 
        parent[a] = find(parent[a])
        return parent[a]
    
def union(a, b) : 
    
    # a, b의 대표노드를 구한다 
    a = find(a)
    b = find(b)
    
    if a != b : 
        parent[b] = a # 서로 다른 집합에 속해있다면
                      # b가 a의 집합에 속하도록 한다
                      
def checkSame(a, b) : # 두 원소가 같은 집합에 속해 있는지 확인하는 함수 
    
    a = find(a)
    b = find(b)
    
    if a == b : 
        return True 
    
    return False

for i in range(0, N+1) : 
    parent[i] = i 
    
for i in range(M) : 
    
    question, a, b = map(int, input().split())
    
    if question == 0 : 
        union(a, b)
    
    else : 
        if checkSame(a, b) : # 두 노드가 서로 같은 집합에 속해 있는지 확인
            print('YES')
        
        else : 
            print('NO')