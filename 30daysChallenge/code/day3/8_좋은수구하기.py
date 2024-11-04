import sys
input = sys.stdin.readline 

N = int(input()) # 데이터 개수 
Result = 0 # 좋은 수의 개수를 저장하는 변수 

# 숫자 데이터를 리스트로 저장해서 정렬 
A = list(map(int, input().split()))
A.sort() 

for k in range(N) : 
    find = A[k]
    i = 0
    j = N-1

    while i < j : 
        if A[i] + A[j] == find : 

            if i != k and j != k : 
                Result = Result + 1 
                break 

            elif i == k :
                i = i + 1

            else :
                j = j + 1

        elif A[i] + A[j] < find : 
            i = i + 1
        
        else : 
            j = j - 1

print(Result)

