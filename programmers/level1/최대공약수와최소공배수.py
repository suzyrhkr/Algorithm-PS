from math import gcd

def solution(n, m):
    GCD = gcd(n,m)
    LCM = n*m//GCD
    return [GCD, LCM]