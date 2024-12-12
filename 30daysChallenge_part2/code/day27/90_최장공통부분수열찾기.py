A = list(input())
A.pop() # \n 문자열 제거

B = list(input())
B.pop() # \n 문자열 제거

DP = [[0 for j in range(len(B) + 1)] for i in range(len(A) + 1)]
Path = []

for i in range(1, len(A) + 1) : 
    for j in range(1, len(B) + 1) : 
        if A[i-1] == B[j-1] : 
            
            DP[i][j] = DP[i-1][j-1] + 1 
            
        else : 
            DP[i][j] = max(DP[i-1][j], DP[i][j-1])
            
print(DP[len(A)][len(B)])

def getText(row, column) : 
    if row == 0 or column == 0 : 
        return 
    
    if A[row - 1] == B[column - 1] : 
        Path.append(A[row-1])
        getText(row-1, column-1)
        
    else :
        if DP[row-1][column] > DP[row][column-1] : 
            getText(row-1, column)
            
        else : 
            getText(row, column-1)
            
getText(len(A), len(B))

for i in range(len(Path)-1, -1, -1) : 
    print(Path.pop(i), end = '')
    
print()