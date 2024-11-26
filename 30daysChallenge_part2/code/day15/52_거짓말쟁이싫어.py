N, M = map(int, input().split())
true_people = list(map, input().split())

T = true_people[0]
del true_people[0]

result = 0
party = [[] for _ in range(M)]

parent = [0] * (N+1)

for i in range(N+1) : 
    parent[i]

def find(a) : 

    if a == parent[a] : 
        return a 
    
    else : 
        parent[a] = find(parent[a])
        return parent[a]
    
def union(a, b) : 

    a = find(a)
    b = find(b)

    if a != b : 
        parent[b] = a 

def checkSame(a, b) : 

    a = find(a)
    b = find(b)

    if a == b : 
        return True 
    
    else : 
        return False
    
for i in range(M) : 

    party[i] = list(map(int, input().split()))

    del party[i][0]


for i in range(M) : 
    firstPerson = party[i][0]

    for j in range(1, len(party[i])) : 
        union(firstPerson, party[i][j])

for i in range(M) : 

    isPossible = True 
    firstPerson = party[i][0]

    for j in range(len(true_people)) : 

        if find(firstPerson) == find(true_people[j]) : 
            isPossible = False
            break

    if isPossible : 
        result += 1 

print(result)