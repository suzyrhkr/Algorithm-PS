def solution(x):
    total = sum(list(map(int, str(x))))
    return x%total==0