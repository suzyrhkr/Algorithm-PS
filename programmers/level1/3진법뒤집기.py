def solution(n):
    answer = 0
    num = ''

    while 0<n:
        num += str(n%3)
        n=n//3

    num = int(num)
    
    i=0
    while 0<num:
        mod = num%10
        num = num//10
        answer += mod*(3**i)
        i+=1

    return answer

#---other solution---

def solution(n):
    answer = 0
    num = ''

    while 0<n:
        num += str(n%3)
        n=n//3

    answer = int(num, 3)
    
    return answer