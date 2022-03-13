class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start, end = 0, 0
        N = len(nums)
        min_length = float('inf')
        
        while(start<=end):
            if N < end:
                break
            subarray = nums[start:end]
            array_sum = sum(subarray)
            if array_sum < target:
                end +=1
            else:
                min_length = min(min_length, len(subarray))
                start += 1

        return min_length if min_length!=float('inf') else 0