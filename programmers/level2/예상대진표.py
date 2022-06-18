import math

def solution(n,a,b):
    answer = 0

    while True:
        if a == b:
            break
        a = math.ceil(a/2)
        b = math.ceil(b/2)
        answer += 1

    return answer