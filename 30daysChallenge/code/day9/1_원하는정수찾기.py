# A에 데이터 삽입
N = int(input())

A = list(map(int, input().split(' ')))
A.sort()

M = int(input())

targets = list(map(int, input().split(' ')))

def binarySearch(start_idx, end_idx, target) : 
    
    if start_idx > end_idx : 
        return 0
    
    mid = int((start_idx + end_idx) / 2)
    
    if target == A[mid] : 
        return 1
    
    elif target < A[mid] : 
        return binarySearch(start_idx, mid-1, target)
        
    elif target > A[mid] : 
        return binarySearch(mid+1, end_idx, target)
    
for target in targets : 
    print(binarySearch(0, N-1, target))