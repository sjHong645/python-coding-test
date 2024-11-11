N = int(input())
K = int(input())

start = 1; end = K; answer = 0

while start <= end : 
    middle = int((start + end)/2)
    count = 0
    
    for i in range(1, N+1) : 
        count += min(int(middle / i), N)
        
    if count < K : 
        start = middle + 1 
    
    else : 
        end = middle - 1
        answer = middle

print(answer)