
F = [0] * 21
S = [0] * 21 
visited = [False] * 21
N = int(input())
F[0] = 1

# 팩토리얼 값 초기화 
for i in range(1, N+1) : 
    F[i] = F[i-1] * i

inputList = list(map(int, input().split())) 

# 소문제 1 해결
if inputList[0] == 1 : 

    K = inputList[1] 

    for i in range(1, N+1) : 
        cnt = 1 
        for j in range(1, N+1) : 
            if visited[j] : # 이미 사용한 숫자는 넘어간다
                continue
            if K <= cnt * F[N-i] : # 주어진 K에 따라 각 자리에 들어갈 수 있는 숫자 찾기 
                K -= (cnt - 1) * F[N-i]
                S[i] = j
                visited[j] = True 
                break
            cnt += 1
    
    for i in range(1, N+1) : 
        print(S[i], end = ' ')

# 소문제 2 해결
else :
    K = 1 
    for i in range(1, N+1) : 
        cnt = 0
        for j in range(1, inputList[i]) : 
            if not visited[j] : 
                cnt += 1 # 미사용 숫자 개수만큼 카운트 
        K += cnt * F[N-i] # 자릿수에 따라 순서 더하기 
        visited[inputList[i]] = True 

    print(K)