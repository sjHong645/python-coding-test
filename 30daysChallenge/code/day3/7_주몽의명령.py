
N = int(input())
M = int(input())

A = list(map(int, input().split()))
A.sort()

i = 1; j = N-1; count = 0

while i < j : 
    if A[i] + A[j] > M : 
        j -= 1

    elif A[i] + A[j] < M : 
        i += 1

    else : 
        i += 1; j -= 1; count += 1

print(count)