
def solution(N, K, array1, array2):
    array1.sort()
    array2.sort(reverse=True)

    for i in range(K):
        array1[i] = array2[i]

    return sum(array1)

print(solution(5, 3, [1,2,5,4,3], [5,5,6,6,5]))