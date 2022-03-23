import copy
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        start, end = 0, len(nums)-1
        result, result_idx = None, []
        nums_copy = copy.deepcopy(nums)
        nums.sort()
        while(start<end):
            sum_ = nums[start] + nums[end]
            if sum_ == target:
                result = nums[start], nums[end]
                break
            elif sum_ < target:
                start += 1
            else:
                end -= 1
        for i in result:
            idx = nums_copy.index(i)
            result_idx.append(idx)
            nums_copy[idx] = None
        return result_idx









