from queue import PriorityQueue

N = int(input())
myQueue = PriorityQueue()

for i in range(N) : 
    request = int(input())

    if request == 0 : 
        if myQueue.empty() : 
            print('0\n')
        else : 
            temp = myQueue.get()
            print(str(temp[1]) + '\n')

    else : 
        # 절댓값을 기준으로 정렬하고
        # 절댓값이 같다면 음수를 먼저 정렬하도록 구성
        myQueue.put((abs(request), request))