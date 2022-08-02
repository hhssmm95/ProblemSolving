cache = []
def top_down(n,m,i,j,pSet):
    if (i,j) in pSet or i <= 0 or j <= 0:
        return 0
    elif cache[i][j] != -1:
        return cache[i][j]
    
    cache[i][j] = top_down(m,n,i-1,j,pSet) + top_down(m,n,i,j-1,pSet)
    return cache[i][j]

def solution1(m,n,puddles):
    global cache
    cache = [[-1]* (m+1) for _ in range(n+1)]
    cache[1][1] = 1
    
    pSet = set((i,j) for (j,i) in puddles)

    answer = top_down(n,m,n,m,pSet)
    return  answer % 1000000007


def solution2(m, n, puddles):
    pSet = set((i,j) for (j,i) in puddles)
    cache = [[0]* (m+1) for _ in range(n+1)]
    cache[1][1] = 1

    for i in range(1,n+1):
        for j in range(1,m+1):
            if (i,j) == (1,1):
                continue
            up = 0 if i == 1 or (i-1,j) in pSet  else cache[i-1][j]
            left = 0 if j == 1 or (i,j-1) in pSet else cache[i][j-1]

            cache[i][j] = up + left
            
    
    return cache[n][m] % 1000000007

print(solution2(4,3,[[2, 2]]))