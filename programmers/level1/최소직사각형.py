def solution(sizes):
    w = [max(x) for x in sizes]
    h = [min(x) for x in sizes]

    return max(w)*max(h)