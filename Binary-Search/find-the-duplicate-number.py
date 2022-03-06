class Solution:     
    def findDuplicate(self, nums: List[int]) -> int:
            nums.sort()
            start, end = 0,len(nums)-1
            
            while (start <= end):
                mid = (start + end) // 2
                print(start, end, mid, nums[mid])
                if nums[mid] < mid+1: 
                    end = mid - 1
                else: 
                    start = mid + 1
            return start