class Solution(object):
    def subsets(self, nums):
        answer = []
        for i in range(len(nums)+1):
            answer.extend(combinations(nums, i))
            
        return answer
            

#---other solution---
class Solution(object):
    def subsets(self, nums):
        answer = []
        N = 2**len(nums)
        for i in range(N):
            bins = bin(i)[2:].rjust(len(nums),"0")
            subset = []
            for n, bin_ in zip(nums, bins):                
                if bin_=='1':
                    subset.append(n)
            answer.append(subset)
        return answer