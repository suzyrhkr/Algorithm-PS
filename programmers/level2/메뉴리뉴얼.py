from itertools import combinations

def solution(orders, course):
    answer = []

    for c in course:
        combination = []
        for order in orders:
            for i in list(combinations(list(order), c)):
                combination.append("".join(sorted(i)))
        
        max_c = 0
        for c in combination:
            max_c = max(max_c, combination.count(c))
        
        for c in set(combination):
            if combination.count(c)==max_c and 1<combination.count(c):
                answer.append(c)
        
    answer.sort()

    return answer

#---other solution---
from collections import Counter
from itertools import combinations

def solution(orders, course):
    answer = []

    for c in course:
        combination = []
        for order in orders:
            for i in list(combinations(list(order), c)):
                combination.append("".join(sorted(i)))
        
        most_ordered = Counter(combination).most_common()
        
        for c in set(combination):
            if combination.count(c)==most_ordered[0][1] and 1<combination.count(c):
                answer.append(c)
        
    answer.sort()

    return answer
