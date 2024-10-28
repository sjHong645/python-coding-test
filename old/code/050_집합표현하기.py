import sys
input = sys.stdin.readline

N, M = map(int, input().split())

parent = [0] * (N+1)

# 대표노드 리스트 초기화 
for i in range(1, N+1) : 
    parent[i] = i


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
        parent[b] = a # 매개변수의 오른쪽 노드의 대표노드가 
                      # 매개변수의 왼쪽 노드가 되도록 설정함 

def checkSame(a, b) : 

    a = find(a) 
    b = find(b)

    if a == b : 
        return True 
    
    else :
        return False
    
for i in range(M) : 
    
    question, a, b = map(int, input().split())

    if question == 0 : 
        union(a, b)

    else :
        if checkSame(a, b) : 
            print('YES')

        else :
            print('NO')