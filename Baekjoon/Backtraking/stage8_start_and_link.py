import sys
input = sys.stdin.readline

N = int(input())

visited = [False]*N
synerge = [list(map(int, input().split())) for _ in range(N)]

team1 = []
team2 = []
min_val = 1e9

def getOffset():
    t1_total = 0
    t2_total = 0
    for i in range(N//2):
        for j in range(N//2):
            if i == j:
                continue
            t1_total += synerge[team1[i]][team1[j]]
            t2_total += synerge[team2[i]][team2[j]]
    
    return abs(t1_total - t2_total)
    

def backtraking(count, start):
    global min_val

    if count == N//2:

        for i in range(N):
            if not visited[i]:
                team2.append(i)

        offset = getOffset()

        if offset < min_val:
            min_val = offset

        team2.clear()

    else:
        for i in range(start, N):
            if not visited[i]:
                team1.append(i)
                visited[i] = True
                backtraking(count+1, i+1)

                team1.remove(i)
                visited[i] = False

backtraking(0, 0)
print(min_val)
