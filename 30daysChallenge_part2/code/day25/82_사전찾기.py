N, M, K = map(int, input().split())
D = [[0 for j in range(202)] for i in range(202)] 

for i in range(201) : 
    for j in range(i+1) : 

        if j == 0 or j == i : 
            D[i][j] = 1
        
        else : 
            D[i][j] = D[i-1][j] + D[i-1][j-1]

            if D[i][j] > 1000000000 : 
                D[i][j] = 1000000001

if D[N+M][M] < K : # 주어진 자릿수로 K번째 수를 만들 수 없는 경우
    print(-1) 

else : 
    while not (N == 0 and M == 0) : 
        if D[N-1+M][M] >= K : 
            print("a", end = '')
            N -= 1 
        else : 
            print("z", end = '')
            K -= D[N-1+M][M]
            M -= 1