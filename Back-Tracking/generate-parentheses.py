class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answer, stack = [], []

        def backtracking(openN, closeN):
            if n == openN == closeN:
                answer.append("".join(stack))

            if openN < n:
                stack.append("(")
                backtracking(openN+1, closeN)
                del stack[-1]

            if closeN < openN:
                stack.append(")")
                backtracking(openN,closeN+1)
                del stack[-1]
        
        backtracking(0,0)
        return answer
        
        