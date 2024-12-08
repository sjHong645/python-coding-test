D = [[0 for j in range(31)] for i in range(31)] 

for i in range(31) : 
    D[i][1] = i
    D[i][0] = 1
    D[i][i] = 1

for i in range(2, 31) : 
    for j in range(1, i) : 
        D[i][j] = D[i-1][j] + D[i-1][j-1]

T = int(input())

for i in range(T) : 
    N, M = map(int, input().split())
    print(D[M][N])