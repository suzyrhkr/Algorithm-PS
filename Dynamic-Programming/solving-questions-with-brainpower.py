class Solution(object):
    def mostPoints(self, questions):
        n = len(questions)
        dp = [0]*(n+1)
        max_value = 0
        
        for i in range(n-1,-1,-1):
            min_value = min(n, i+questions[i][1]+1)
            dp[i] = max(questions[i][0] + dp[min_value], dp[i+1])
            
        return dp[0]
            
        