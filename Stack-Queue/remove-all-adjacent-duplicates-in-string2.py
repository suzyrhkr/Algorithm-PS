class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        
        for ch in s:
            if not stack or ch!=stack[-1][0]:
                stack.append([ch, 1])
                continue
            
            if ch == stack[-1][0]:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
   
        answer = [x[0]*x[1] for x in stack]
        return "".join(answer)
        
    