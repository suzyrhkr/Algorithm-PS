class Solution(object):
    def lastStoneWeightII(self, stones):
	
        req = sum(stones)//2        
        dp = [0 for i in range(req+1)]
        
        for nums in stones:
            for w in range(req, nums-1, -1): 
				dp[w] = max(dp[w], dp[w-nums] + nums)

        return sum(stones) - 2*dp[req]