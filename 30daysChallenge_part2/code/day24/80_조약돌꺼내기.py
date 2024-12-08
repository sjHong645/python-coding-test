D = [0] * 51
probability = [0] * 51

M = int(input())
D = list(map(int, input().split()))
T = 0

# 조약돌 개수 더하기 
for i in range(M) : 
    T += D[i]

K = int(input())
answer = 0

for i in range(M) : 
    
    if D[i] >= K : 
        probability[i] = 1

        for k in range(K) : 
            probability[i] = probability[i] * (D[i] - k) / (T - k)

        answer += probability[i]

print(answer)