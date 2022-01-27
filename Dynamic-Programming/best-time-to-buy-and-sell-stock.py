#---Time Limit Exceeded---
class Solution(object):
    def maxProfit(self, prices):
        dp = [0]*len(prices)
                
        for i, p in enumerate(prices[:-1]):
            max_val = max(prices[i+1:])
            if p<max_val:
                dp[i] = max_val-p
            else:
                dp[i] = 0
                
        return max(dp)

#---other solution(O(n))---
class Solution(object):
    def maxProfit(self, prices):
        profit = 0
        min_val = prices[0]
        
        for p in prices[1:]:
            profit = max(profit, p-min_val)
            min_val = min(min_val, p)
            
        return profit
    