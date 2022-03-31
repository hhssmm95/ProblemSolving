import sys
input = sys.stdin.readline

def merge(left, right):
    i = 0
    j = 0

    sorted_array = []

    while (i < len(left)) and (j < len(right)):
        if left[i] > right[j]:
            sorted_array.append(right[j])
            j+=1
        else:
            sorted_array.append(left[i])
            i+=1

    while i < len(left):
        sorted_array.append(left[i])
        i+=1
    while j < len(right):
        sorted_array.append(right[j])
        j+=1
    
    return sorted_array


def merge_sort(array):

    if len(array) <= 1:
        return array

    mid = len(array)//2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])

    return merge(left, right)

N = int(input())

array = []

for i in range(N):
    array.append(int(input()))

result = merge_sort(array)
for i in result:
    print(i)