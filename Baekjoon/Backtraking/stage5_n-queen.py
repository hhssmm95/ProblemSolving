import sys
input = sys.stdin.readline

N = int(input())
row = [-1]*N
case = 0

def DFS(curr):
    global case
    if  curr >= N:
        case += 1 
        return
    
    for i in range(N):
            row[curr] = i
            
            for j in range(curr):
                if row[j] == row[curr] or (row[curr] - curr) == (row[j] - j) or (row[curr] + curr) == (row[j] + j):
                    break
            else:
                DFS(curr+1)
        
DFS(0)
print(case)