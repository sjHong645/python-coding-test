import sys

dp = [[[sys.maxsize for k in range(5)] for j in range(5)] for i in range(100001)]

# 한 발을 이동할 때 드는 힘을 미리 저장함
# mp[1][2] : 1->2로 이동할 때 드는 힘 
mp = [
    [0, 2, 2, 2, 2], 
    [2, 1, 3, 4, 3], 
    [2, 3, 1, 3, 4], 
    [2, 4, 3, 1, 3], 
    [2, 3, 4, 3, 1]
]

s = 1 
dp[0][0][0] = 0

inputList = list(map(int, input().split()))
index = 0

while inputList[index] != 0 : 
    n = inputList[index]
    
    for i in range(5) : 
        if n == i : # 두 발이 같은 자리에 있는 경우
                    # 그런 경우는 없기 때문에 넘어간다
            continue
    
        for j in range(5) : 
            
            # 오른발을 j -> n으로 옮겼을 때 드는 최소 힘 저장  
            dp[s][i][n] = min(dp[s-1][i][j] + mp[j][n], dp[s][i][n])
            
    for j in range(5) : 
        if n == j : # 두 발이 같은 자리에 있는 경우는 없다
            
            continue
        
        for i in range(5) : 
            
            # 왼발을 i -> n으로 옮겼을 때 드는 최소 힘 저장
            dp[s][n][j] = min(dp[s-1][i][j] + mp[i][n], dp[s][n][j])
            
    s += 1 
    index += 1 
    
s -= 1 # 마지막 이동 횟수로 index값 조정
result = sys.maxsize

for i in range(5) : 
    for j in range(5) : 
        result = min(result, dp[s][i][j]) # 모두 수행한 후 최소값 찾기
        
print(result)