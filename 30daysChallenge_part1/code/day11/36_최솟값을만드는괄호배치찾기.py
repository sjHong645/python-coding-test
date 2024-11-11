answer = 0
A = list(map(str, input().split("-")))

def sum(i) : 
    sum = 0
    temp = str(i).split("+")

    for i in temp : 
        sum += int(i)

    return sum

for i in A : 

    temp = sum(A[i])

    if i == 0 : 
        answer += temp
    
    else : 
        answer -= temp

print(answer)