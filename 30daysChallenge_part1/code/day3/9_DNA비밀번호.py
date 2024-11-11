checkList = [0] * 4 
myList = [0] * 4
checkSecret = 0

def myAdd(c) : 
    global checkList, myList, checkSecret

    if c == 'A' : 
        myList[0] += 1 
        if myList[0] == checkList[0] : 
            checkSecret += 1

    elif c == 'C' : 
        myList[1] += 1 
        if myList[1] == checkList[1] : 
            checkSecret += 1

    elif c == 'G' : 
        myList[2] += 1 
        if myList[2] == checkList[2] : 
            checkSecret += 1

    else : # c == 'T' 
        myList[3] += 1 
        if myList[3] == checkList[3] : 
            checkSecret += 1

def myRemove(c) : 
    global checkList, myList, checkSecret

    if c == 'A' : 
        if myList[0] == checkList[0] : 
            checkSecret -= 1
        myList[0] -= 1 

    elif c == 'C' : 
        if myList[1] == checkList[1] : 
            checkSecret -= 1
        myList[1] -= 1 

    elif c == 'G' :  
        if myList[2] == checkList[2] : 
            checkSecret -= 1
        myList[2] -= 1

    else : # c == 'T' 
        if myList[3] == checkList[3] : 
            checkSecret -= 1
        myList[3] -= 1 

S, P = map(int, input().split())
Result = 0

A = list(input())
checkList = list(map(int, input().split()))

# 초기 상태 리스트를 만들기 
# 지금 현재 checkList에서 A, C, G, T 중에서 0인 값이 있다는 건
# 이미 해당 문자는 비밀번호 조건을 만족한거니까 checkSecret값을 1 증가
for i in range(4) : 
    if checkList[i] == 0 : 
        checkSecret += 1

# 초기 상태의 현재 상태 리스트와 비밀번호 체크 리스트값을 넣는 부분 
for i in range(P) : 
    myAdd(A[i])

# 이미 비밀번호가 여기서 만족되었다면 경우의 수를 1 증가시킨다
if checkSecret == 4 : 
    Result += 1 

# 윈도우를 한 칸씩 이동하면서 
# 비밀번호 체크 리스트와 비교하면서 비밀번호 유효성을 판단한다
for i in range(P, S) : 
    j = i - P 

    # 이 부분에서 현재 상태 리스트를 업데이트 한다.
    myAdd(A[i])
    myRemove(A[j])

    if checkSecret == 4 : 
        Result += 1 

print(Result)