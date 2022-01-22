class Solution(object):
    def singleNumber(self, nums):

        stack = []
        nums.sort()
        
        for n in nums:
            if not stack:
                stack.append(n)
                continue
                
            if n==stack[-1]:
                stack.pop()
            else:
                stack.append(n)
        
        return stack[0]

#---other solution(using only constant extra space)---
class Solution(object):
    def singleNumber(self, nums):
        a=0
        for n in nums:
            a = a^n
        return a