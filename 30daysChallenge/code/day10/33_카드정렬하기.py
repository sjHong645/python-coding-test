from queue import PriorityQueue

N = int(input())
pq = PriorityQueue()

for _ in range(N) :
    data = int(input())
    pq.put(data)
    
data1 = 0; data2 = 0; sum = 0

while pq.qsize() > 1 : 
    
    # 2개의 카드 묶음을 큐에서 뽑는다
    data1 = pq.get()
    data2 = pq.get()
    
    # 2개의 카드 묶음을 합치는데 필요한 비교횟수를 결과값에 더한다
    temp = data1 + data2
    sum += temp
    
    # 2개의 카드 묶음 합을 우선순위 큐에 다시 넣는다
    pq.put(temp)
    
print(sum)