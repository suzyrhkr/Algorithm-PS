#---시간 초과 solution---

def solution(n):
    answer = 0
    for num in range(2, n+1):
        cnt = 0
        for j in range(1, int(num**0.5+1)):
            if num%j==0:
                cnt+=1
        if cnt == 1:
            answer += 1
    return answer

#---other solution(에라토스테네스 체)---

def solution(n):
    num = set(range(2, n+1))
    
    for i in range(2, n+1):
        if i in num:
            num -= set(range(2*i, n+1, i))

    return len(num)