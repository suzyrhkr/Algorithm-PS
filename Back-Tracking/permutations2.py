class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res, visited = [], [False]*len(nums)
        nums.sort()
        self.dfs(nums, visited, [], res)
        return res
    
    def dfs(self, nums, visited, path, res):
        if len(nums) == len(path):
            res.append(path)
            return 
        
        for i in range(len(nums)):
            if not visited[i]: 
                if i!=0 and not visited[i-1] and nums[i] == nums[i-1]:  
                    continue
                visited[i] = True
                self.dfs(nums, visited, path+[nums[i]], res)
                visited[i] = False