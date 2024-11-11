from collections import deque

N = int(input())
myQueue = deque()

# 1부터 N까지 큐에 저장
for i in range(1, N+1) : 
    myQueue.append(i)

while len(myQueue) > 1 : 
    myQueue.popleft() # 과정 1 
    myQueue.append(myQueue.popleft()) # 과정 2 

print(myQueue[0])
