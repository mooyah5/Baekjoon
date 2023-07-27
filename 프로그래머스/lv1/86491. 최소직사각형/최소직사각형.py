def solution(sizes):
    sizes = [sorted(size) for size in sizes]
    a, b = zip(*sizes)
    return max(a) * max(b)