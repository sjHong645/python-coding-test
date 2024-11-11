from collections import deque

N, L = map(int, input().spilt()) # 데이터 개수, 윈도우 크기 

mydeq = deque() # 문제풀이를 위해 사용할 덱
                # 덱에는 (인덱스, 숫자) 튜플을 저장할 거다

now = list(map(int, input().split())) # 입력받은 데이터 

for i in range(N) : 

    # 덱의 마지막 위치에서부터 현재 값보다 큰 값은 덱에서 제거 
    while mydeq and mydeq[-1][1] > now[i]: 
        mydeq.pop()

    # 덱의 마지막 위치에 현재 값 저장 
    mydeq.append((i, now[i]))    

    # 덱의 1번째 위치에서부터 L의 범위를 벗어난 값 제거 
    if mydeq[0][0] <= i-1 : 
        mydeq.popleft()

    # 현재 범위의 최소값 출력 
    print(mydeq[0][1], end = ' ')