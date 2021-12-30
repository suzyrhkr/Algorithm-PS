def solution(price, money, count):
    sum=0
    for cnt in range(1, count+1):
        sum += price*cnt 
  
    return abs(money - sum) if money-sum<0 else 0

#---other solution---

def solution(price, money, count):
    return max(0,price*(count+1)*count//2-money)
