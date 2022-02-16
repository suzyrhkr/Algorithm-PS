from collections import deque

def correct_str(s):
    stack = []
    
    for ch in s:
        if ch == '(' or ch == '{' or ch == '[':
            stack.append(ch)
        else:
            if len(stack) == 0: 
                return False
            x = stack.pop()
            
            if ch == ')' and x != '(':
                return False
            elif ch == ')' and x != '(':
                return False
            elif ch == '}' and x != '{':
                return False

    return True if not stack else False
    
def solution(s):
    answer = 0
    
    str = deque()
    for ch in s:
        str.append(ch)
  
    for i in range(len(str)):
        str.rotate(-1)
        if correct_str(str):
            answer+=1
            
    return answer