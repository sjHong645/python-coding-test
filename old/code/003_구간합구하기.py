import sys 

input = sys.stdin.readline 

N, M = map(int, input().split()) 

numbers = list(map(int, input().split())) 

prefix_sum = [0]

temp = 0 # 구간 합 배열의 첫 번째 값으로 초기화 

for i in numbers : 
    temp = temp + i 
    prefix_sum.append(temp) # 계산을 통해 나온 결과로 구간 합 추가 

for i in range(M) : 
    
    start, end = map(int, input().split())
    print(prefix_sum[end] - prefix_sum[start - 1])
    