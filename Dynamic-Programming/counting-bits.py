class Solution(object):
    def countBits(self, n):
        ans = []
        
        for num in range(n+1):
            cnt = 0
            # counting 1 using bit manipulation
            while num!=0:
                num = num&(num-1)
                cnt += 1
            
            ans.append(cnt)
        
        return ans

#---other solution(dynamic programming)---
class Solution(object):
    def countBits(self, n):
        dp = [0] * (n + 1)
        offset = 1
        
        for i in range(1, n+1):
            if offset * 2 == i:
                offset = i
                
            dp[i] = 1 + dp[i-offset]
            
        return dp