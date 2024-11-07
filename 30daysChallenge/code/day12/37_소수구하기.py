import math

M, N = map(int, input().split())

A = [0] * (N+1) # 소수인지 아닌지를 저장할 리스트

for i in range(2, N+1) : 
    A[i] = i # 소수이면 숫자 남기고
             # 소수 아니면 0을 저장한다.


for i in range(2, int(math.sqrt(N)) + 1) : # 제곱근까지만 수행

    if A[i] == 0 : 
        continue

    for j in range(i+1, N+1, i) : # 소수의 배수는 소수가 아니기 때문에 지운다
        A[j] = 0

# M ~ N 범위에서 소수값 출력 
for i in range(M, N+1) : 
    if A[i] != 0 : 
        print(A[i])