def k_prime(n, k):
    answer = ''
    
    while 0 < n:
        answer += str(n % k)
        n //= k
        
    return answer[::-1]
    
def isPrime(n):
    cnt = 0
    if n < 2: 
        return False
    
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            print(n, i)
            cnt += 1
    
    return True if cnt == 0 else False

def solution(n, k):
    answer = 0
    ret = k_prime(n, k).split("0")

    for i, num in enumerate(ret):
        if num == "":
            continue
        if isPrime(int(num)):
            answer += 1
    
    return answer