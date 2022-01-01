#---run time error---

from itertools import combinations

def solution(d, budget):
    answer = 0
    num = len(d)
    total = []

    while 0<num:
        combination = combinations(d, num)
        
        for c in combination:
            if sum(c)==budget:
                return num
            elif sum(c) < budget:
                total.append((num,sum(c)))

        num-=1

    answer = max(total, key=lambda x:x[1])[0]
    return answer

#---other solution(time complexity: O(n))---

def solution(d, budget):
    answer = 0
    d.sort()

    for i in range(len(d)):
        if d[i]<=budget:
            answer+=1
            budget-=d[i]
        else:
            break
    return answer