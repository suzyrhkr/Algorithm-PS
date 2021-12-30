def solution(n):
    sqrt_ = int(n**0.5)
    return (sqrt_+1)**2 if sqrt_**2==n else -1