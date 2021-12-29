from itertools import combinations

def solution(numbers):
    answer = []
    combination = list(combinations(numbers, 2))

    for x, y in combination:
        answer.append(x+y)

    answer = sorted(list(set(answer)))
    return answer