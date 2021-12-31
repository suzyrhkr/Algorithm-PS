def findLCD(a, b):
    d = 0

    for n in range(1, min(a,b)+1):
        if a%n==0 and b%n==0:
            d = n
    lcd = d * (a//d) * (b//d)

    return lcd

def solution(arr):
    
    while 1<len(arr):
        a = arr.pop(0)
        b = arr.pop(0)

        arr.append(findLCD(a,b))
        arr = list(set(arr))
    
    return arr[0]

#---other solution---
from math import gcd

def solution(num):
    answer = 1
    for i in range(len(num)):
        answer = (num[i] * answer) // (gcd(num[i], answer))
  
    return answer