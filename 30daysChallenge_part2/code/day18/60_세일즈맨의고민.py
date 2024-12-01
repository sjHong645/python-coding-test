import sys

N, start_city, end_city, M = map(int, input().split())

edges = []
distance = [-sys.maxsize] * N

for _ in range(M) : 
    start, end, price = map(int, input().split())
    edges.append((start, end, price))

cityMoney = list(map(int, input().split()))

# 변형된 벨만 포드 수행 
distance[start_city] = cityMoney[start_city]

# 양수 사이클이 전파 되도록 충분히 큰 수로 반복 
for i in range(N+101) : 
    for start, end, price in edges : 
        if distance[start] == -sys.maxsize : 
            continue
        elif distance[start] == sys.maxsize : 
            distance[end] = sys.maxsize
        
        # 더 많은 돈을 벌 수 있는 새로운 경로가 있는 경우 값 업데이트
        elif distance[end] < distance[start] + cityMoney[end] - price : 
            distance[end] = distance[start] + cityMoney[end] - price

            if i > N-1 : 
                distance[end] = sys.maxsize

if distance[end_city] == -sys.maxsize : 
    print('gg')

elif distance[end_city] == sys.maxsize : 
    print('Gee')

else :
    print(distance[end_city])