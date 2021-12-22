def solution(nums):
    answer = 0

    def isPrime(number):
        cnt=0
        for i in range(1,number):
            if number % i ==0:
                cnt+=1
        
        return True if cnt==1 else False

    for i in range(0,len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                ret = isPrime(nums[i] + nums[j] + nums[k])
                if ret == True:
                    answer += 1
    
    return answer



# ---other solution---
from itertools import combinations

def solution(nums):
    answer=0
    
    def isPrime(number):
        cnt=0
        for i in range(1, int(number**0.5)+1):
            if number % i==0:
                cnt+=1
        
        return True if cnt==1 else False

    for combination in combinations(nums, 3):
        if isPrime(sum(combination)):
            answer += 1

    return answer
    