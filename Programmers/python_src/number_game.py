import heapq

def solution(A, B):
    answer = 0

    A.sort(reverse=True)
    bHeap = []
    for b in B:
        heapq.heappush(bHeap, -b)

    for a in A:
        poppedB = -heapq.heappop(bHeap)
        if a < poppedB:
            answer+=1
        else:
            heapq.heappush(bHeap, -poppedB)

    return answer