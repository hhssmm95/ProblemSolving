def find_root(parent, x):
    if parent[x] != x:
        parent[x] = find_root(parent, parent[x])
    return parent[x]

def union_node(parent, a, b):
    A = find_root(parent, a)
    B = find_root(parent, b)

    if A < B:
        parent[B] = A
    else:
        parent[A] = B

    return
        
def kruskal(n, m, data):
    parent = [i for i in range(n+1)]
    mst = []

    data.sort(key=lambda x: x[2])

    for i in data:
        if find_root(parent, i[0]) != find_root(parent, i[1]):
            union_node(parent, i[0], i[1])
            mst.append(i)

    for i in mst:
        print(f"{i[0]} - {i[1]}    ({i[2]})")



kruskal(7, 9, [(1,2,29), (1,5,75), (2,3,35), (2,6,34), (3,4,7), (4,6,23), (4,7,13), (5,6,53), (6,7,25)])