N = int(input())
IsBipart = True 

def DFS(node) : 
    global IsBipart 
    visited[node] = True 

    for i in A[node] : 
        if not visited[i] : 

            # 인접 노드는 같은 집합이 아니라서 다른 집합으로 처리한다
            check[i] = (check[node] + 1) % 2
            DFS(i)

        # 이미 방문한 노드가 현재 노드와 같은 집합이 아니라면 이분 그래프가 아니다
        elif check[node] == check[i] : 
            IsBipart = False

for _ in range(N) : 
    V, E = map(int, input().split())
    A = [[] for _ in range(V+1)]
    visited = [False] * (V+1)
    check = [0] * (V+1)
    IsBipart = True 

    for i in range(E) : 
        S, E = map(int, input().split())
        A[S].append(E)
        

    for i in range(1, V+1) : 
        if IsBipart : 
            DFS(i)

        else : 
            break

    if IsBipart : 
        print('YES')
    else : 
        print('NO')