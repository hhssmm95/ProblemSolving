'''
7*5
0000000
000-000
0s0-0e0
000-000
0000000
'''
import heapq
from math import sqrt

R = [1,-1,0,0,-1,-1,1,1]
C = [0,0,1,-1,-1,1,-1,1]

n = 5
m = 7
board = [['0000000'], ['000-000'],['0s0-0e0'],['000-000'],['0000000']]
start = (2,1)
end = (2,5)

class Node:
    def __init__(self, pos = None, parent = None):
        self.parent = parent
        self.pos = pos

        self.f = 0
        self.g = 0
        self.h = 0

def getDirectDistance(posA, posB):
    return sqrt(pow(posB[0] - posA[0],2) + pow(posB[1] - posA[1],2))

def aStar():
    result = ['0' * m for _ in range(n)]
    opened = []
    closed = {}
    heapq.heappush(opened, [0,0,0,start,(-1,-1)])

    while opened:
        curr_f, curr_g, curr_h, curr_pos, prev_pos = heapq.heappop(opened)

        closed[curr_pos] = opened[curr_pos]
        opened.pop()

        for dir in range(8):
            nr = curr_pos[0] + R[dir]
            nc = curr_pos[1] + C[dir]

            if 0 <= nr < n and 0 <= nc < m and (nr,nc) not in closed: 
                g = getDirectDistance(curr_pos, (nr,nc))
                h = getDirectDistance(end, (nr,nc))
                f = g+h

                if (nr,nc) in opened and opened[(nr,nc)][1] > g:
                    opened[(nr,nc)] = [f,g,h,(nr,nc),curr_pos]


            

