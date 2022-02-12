class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k==len(num):
            return "0"
    
        stack = []
        
        for n in num:
            while stack and k!=0 and n<stack[-1]:
                del stack[-1]
                k -= 1
            
            if not stack and n=="0":
                continue
            stack.append(n)
        
        return "0" if not stack or k>=len(stack) else "".join(stack[:len(stack)-k])