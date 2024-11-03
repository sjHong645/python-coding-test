
n, m = map(int, input().split())

A = [[0] * (n+1)] # 0번째 행에 0을 채운 걸로 원본 리스트를 선언 및 초기화
D = [[0] * (n+1) for _ in range(n+1)]

# 원본 리스트의 1번째 행부터 데이터를 저장
for i in range(n) : 
    A_row = [0] + [int(x) for x in input().split()]
    A.append(A_row)

for i in range(1, n+1) : 
    for j in range(1, n+1) : 
        # 합 배열 구하기 
        D[i][j] = D[i][j-1] + D[i-1][j] - D[i-1][j-1] + A[i][j]

for _ in range(m) : 

    x1, y1, x2, y2 = map(int, input().split())

    result = D[x2][y2] - D[x1-1][y2] - D[x2][y1-1] + D[x1-1][y1-1]

    print(result)