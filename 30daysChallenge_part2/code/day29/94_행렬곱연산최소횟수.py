import sys

N = int(input()) # 행렬 개수
M = [] # 행렬을 저장하는 리스트 

# i ~ j번째 행렬까지 최소 연산 횟수를 저장한 테이블 
D = [[-1 for j in range(N+1)] for i in range(N+1)] 

M.append((0, 0))

for i in range(N) : 
    x, y = map(int, input().split())
    M.append((x, y))
    
def execute(start, end) : 
    
    result = sys.maxsize 
    
    if D[start][end] != -1 : 
        return D[start][end]
    
    # 행렬 1개의 곱셈 연산
    if start == end : 
        return 0 
    
    # 행렬 2개의 곱셈 연산
    if start + 1 == end : 
        return M[start][0] * M[start][1] * M[end][1]
    
    # 행렬 3개 이상의 곱셈 연산 
    for i in range(start, end) : 
        result = min(result, 
                     M[start][0] * M[i][1] * M[end][1] + execute(start, i) + execute(i+1, end))
        
    D[start][end] = result 
    
    return D[start][end]

print(execute(1, N))