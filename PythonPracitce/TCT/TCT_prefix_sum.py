def prefix_sum(query, array):
    left = query[0]
    right = query[1]

    prefix_array = [0]

    sum_val = 0

    for i in array:
        sum_val += i
        prefix_array.append(sum_val)


    print(prefix_array[right] - prefix_array[left-1])

prefix_sum((3,4), [10,20,30,40,50])


