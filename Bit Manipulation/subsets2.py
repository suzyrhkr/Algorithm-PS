class Solution(object):
    def subsetsWithDup(self, nums):
        answer = []
        
        for i in range(2**len(nums)):
            binary = bin(i)[2:].rjust(len(nums),"0")
            subset = []
            
            for n, b in zip(nums, binary):
                if b=='1':
                    subset.append(n)
            
            subset.sort()
            if subset not in answer:
                answer.append(subset)
        
        return answer

#---other solution---
class Solution(object):
    def singleNumber(self, nums):
        a=0
        for n in nums:
            a = a^n
        return a
                    