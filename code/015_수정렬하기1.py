N = int(input())
A = [0] * N

# 리스트 A에 입력값 저장하기 
for i in range(N) : 
    A[i] = int(input())

for i in range(N-1) : 
    for j in range(N-1-i) : 
        if A[j] > A[j-1] : 
            temp = A[j]
            A[j] = A[j-1]
            A[j-1] = temp

for i in range(N) : 
    print(A[j])