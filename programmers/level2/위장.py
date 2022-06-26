from collections import defaultdict

def solution(clothes):
    answer = 1
    closet = defaultdict(int)
    
    for name, category in clothes:
        closet[category] += 1
    
    for key in closet:
        answer *= (closet[key] + 1)
    
    return answer - 1