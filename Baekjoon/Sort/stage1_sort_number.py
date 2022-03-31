N = int(input())

array = []

for i in range(N):
    array.append(int(input()))
array.sort()

for i in array:
    print(i)