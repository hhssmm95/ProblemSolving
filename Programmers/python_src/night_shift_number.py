import heapq


def solution(n, works):
    answer = 0

    heap_works = []
    for work in works:
        heapq.heappush(heap_works, -work)

    for i in range(n):
        heap_max = heapq.heappop(heap_works)
        heapq.heappush(heap_works, heap_max+1)

    for work in heap_works:
        if work < 0:
            answer += pow(work,2)

    return answer

print(solution(4, [4,3,3]))