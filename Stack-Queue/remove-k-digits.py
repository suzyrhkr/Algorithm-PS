class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num)==k:
            return "0"
    
        stack = []
        
        for n in num:
            while stack and k!=0 and n<stack[-1]:
                del stack[-1]
                k -= 1
            stack.append(n)
            
        stack = "".join(stack).lstrip("0")
        
        # if stack is empty or k remains..
        if not stack or len(stack)<=k:
            return "0"
        
        else:
            return stack[:len(stack)-k]