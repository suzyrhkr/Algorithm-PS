def solution(n):
    answer = 0
    nums = list(range(1,n+1))
    
    for i in range(n):
        range_sum = 0
        for j in range(i, n):
            range_sum += nums[j]
            if range_sum == n:
                answer += 1
                break
            if n < range_sum:
                break
    
    return answer