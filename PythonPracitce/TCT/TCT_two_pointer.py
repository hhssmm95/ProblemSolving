def two_pointer1(M, N, array):
    count = 0
    interval_sum = 0
    end = 0

    for start in range(N):
        while interval_sum < M and end <N:
            interval_sum += array[end]
            end+=1
        if interval_sum == M:
            count+=1
        interval_sum -= array[start]



# def two_pointer2(M, N, array):
#     head = 0
#     tail = 0

#     count = 0

#     while head < N:
#         summ = sum(array[head:tail+1])
#         if summ == M:
#             count+=1
#             head+=1
#         elif summ > M:
#             head+=1
#         elif summ < M:
#             tail+=1

#     print(count)

two_pointer1(5,5,[1,2,3,2,5])

            


