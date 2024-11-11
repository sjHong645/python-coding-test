# https://www.acmicpc.net/problem/2023

import sys

input = sys.stdin.readline

N = int(input()) 

def isPrime(n) : 
    
    for i in range(2, n/2 + 1) : 
        
        if n % i == 0 : 
            return False
    
    return True

def DFS(number) : 
    
    if len(str(number)) == N : 
        print(number)
        
    else : 
        for i in range(1, 10) : 
            
            if i % 2 != 0 and isPrime(10 * number + i) : 
                DFS(10 * number + i)
                
DFS(2);DFS(3);DFS(5);DFS(7)