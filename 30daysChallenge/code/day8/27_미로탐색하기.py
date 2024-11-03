from collections import deque

# (dx[0], dy[0]) = 위쪽으로 1칸
# (dx[1], dy[1]) = 오른쪽으로 1칸
# (dx[2], dy[2]) = 아래쪽으로 1칸
# (dx[3], dy[3]) = 왼쪽으로 1칸
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# N : row, M : column
N, M = map(int, input().split())

A = [[0] * M for _ in range(N)]

visited = [[False] * M for _ in range(N)]

# 그래프 데이터 삽입
for i in range(N) : 
    numbers = list(input()) 
    
    for j in range(M) : 
        A[i][j] = int(numbers[i])
        
# BFS 
def BFS(i, j) : 
    queue = deque()
    
    # (i, j) 방문하면서 시작
    queue.append((i, j))
    visited[i][j] = True 
    
    while queue : 
        now = queue.popleft()
        
        for k in range(4) : 
            
            x = now[0] + dx[k] 
            y = now[1] + dy[k]
            
            # 이웃 좌표가 유효한지 판단 
            # 범위를 넘어서면 판단할 가치가 없다.
            if x >= 0 and y >= 0 and x < N and y < M : 
                
                # (x, y)를 지나갈 수 있고 아직 방문하지 않았다면
                if A[x][y] != 0 and not visited[x][y] : 
                    
                    visited[x][y] = True
                    queue.append((x, y))
                    A[x][y] = A[now[0]][now[1]] + 1
                    
BFS(0, 0)
print(A[N-1][M-1])
