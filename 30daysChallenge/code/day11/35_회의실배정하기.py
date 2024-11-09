N = int(input())
A = [[0] * 2 for _ in range(N)]

for i in range(N) : 
    S, E = map(int, input().split())
    
    A[i][0] = E # 종료 시각을 우선으로 정렬해야 하므로 
                # 0번째에 종료 시각을 저장
    A[i][1] = S 
    
A.sort()

count = 0; end = -1 

for i in range(N) : 
    if A[i][1] >= end : # 앞 회의시간의 종료시각과 겹치지 않는 회의가 나왔다
        end = A[i][0]   # 종료 시각 업데이트
        count += 1

print(count)