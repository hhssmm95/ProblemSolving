def find_root(parent, x):
    if parent[x] != x:
        return find_root(parent, parent[x])
    return x

def union_node(parent, a, b):
    A = find_root(parent, a)
    B = find_root(parent, b)

    if A < B:
        parent[B] = A
    else:
        parent[A] = B

    return