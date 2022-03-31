import heapq
import sys
input = sys.stdin.readline


'''
산술평균 : N개의 수들의 합을 N으로 나눈 값
중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
최빈값 : N개의 수들 중 가장 많이 나타나는 값
범위 : N개의 수들 중 최댓값과 최솟값의 차이
'''
    

N = int(input())
neg_array = []
pos_array = []

max_val = -1e9
min_val = 1e9
sum_val = 0

for i in range(N):
    num = int(input())
    if num > max_val:
        max_val = num
    if num < min_val:
        min_val = num
        
    if num >= 0:
        pos_array.append(num)
    else:
        neg_array.append(-num)    
    sum_val += num

neg_counter = [0]*(abs(min_val)+1)
pos_counter = [0]*(max_val+1)

neg_mode_max = 0
neg_mode = 0
neg_mode_heap = []

pos_mode_max = 0
pos_mode = 1e9
pos_mode_heap = []


for i in neg_array:
    neg_counter[i] += 1
    if neg_counter[i] > neg_mode_max:
        neg_mode_max = neg_counter[i]
        neg_mode_heap.clear()
        heapq.heappush(neg_mode_heap, -i)
    elif neg_counter[i] == neg_mode_max:
        heapq.heappush(neg_mode_heap, -i)
        

for i in pos_array:
    pos_counter[i] += 1
    if pos_counter[i] > pos_mode_max:
        pos_mode_max = pos_counter[i]
        pos_mode_heap.clear()
        heapq.heappush(pos_mode_heap, i)
    elif pos_counter[i] == pos_mode_max:
        heapq.heappush(pos_mode_heap, i)

temp_array = []
for i in range(abs(min_val)+1):
    for j in range(neg_counter[i]):
        temp_array.append(-i)

sorted_array = []
temp_array.reverse()
sorted_array += temp_array

for i in range(max_val + 1):
    for j in range(pos_counter[i]):
        sorted_array.append(i)

mode = 0
if neg_mode_max == 1 and pos_mode_max == 1:
    if len(neg_mode_heap) == 1:
        mode = heapq.heappop(pos_mode_heap)
    else:
        heapq.heappop(neg_mode_heap)
        mode = heapq.heappop(neg_mode_heap)

elif neg_mode_max >= pos_mode_max:
    if len(neg_mode_heap) == 1:
        mode = heapq.heappop(neg_mode_heap)
    else:
        heapq.heappop(neg_mode_heap)
        mode = heapq.heappop(neg_mode_heap)

elif neg_mode_max < pos_mode_max:
    if len(pos_mode_heap) == 1:
        mode = heapq.heappop(pos_mode_heap)
    else:
        heapq.heappop(pos_mode_heap)
        mode = heapq.heappop(pos_mode_heap)

arithmetic_mean = 0 #round(sum_val // N, 0)
if sum_val > 0:
    arithmetic_mean = int(round(sum_val / N, 0))
else:
    arithmetic_mean = -int(round(abs(sum_val) / N, 0))

median = sorted_array[N//2]
Range = max_val - min_val

print(f'{arithmetic_mean}\n{median}\n{mode}\n{Range}')

