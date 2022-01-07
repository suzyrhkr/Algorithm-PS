from itertools import permutations

def isPrime(number):
    cnt=0

    if number in [0,1]:
        return False

    for i in range(1,int(number**0.5)+1):
        if number % i ==0:
            cnt+=1
    
    return True if cnt==1 else False

def solution(numbers):
    answer = 0
    nums = list(numbers)
    p = []
    permutation = []

    for i in range(1, len(nums)+1):
        permutation.extend(list(permutations(nums, i)))

    p = [int(''.join(x)) for x in permutation]

    for i in set(p):
        if isPrime(i):
            answer += 1

    return answer