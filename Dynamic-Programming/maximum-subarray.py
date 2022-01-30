class Solution(object):
    def maxSubArray(self, nums):
        if len(nums) == 1:
            return nums[0]
    
        for i in range(1, len(nums)):
            nums[i] = max(nums[i], nums[i-1] + nums[i])
        
        return max(nums)