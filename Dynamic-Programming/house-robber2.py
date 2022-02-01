class Solution(object):
    def rob(self, nums):
        if len(nums)<=2:
            return max(nums)
        
        dp_1, dp_2 = [0]*(len(nums)-1), [0]*(len(nums))
        
        dp_1[0] = nums[0]
        for i in range(1, len(nums)-1):
            dp_1[i] = max(dp_1[i-2]+nums[i], dp_1[i-1])
            
        dp_2[1] = nums[1]
        for i in range(2, len(nums)):
            dp_2[i] = max(dp_2[i-2]+nums[i], dp_2[i-1])
            
        return(max(dp_1[-1], dp_2[-1]))
        