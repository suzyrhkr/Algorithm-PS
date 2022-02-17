from collections import deque

def correct_str(s):
    stack = []
    
    for ch in s:
        if ch in ['(', '[', '{']:
            stack.append(ch)
            continue
        else:
            if not stack:
                return False
        
        if stack[-1]=='[' and ch==']':
            stack.pop()
        elif stack[-1]=='{' and ch=='}':
            stack.pop()
        elif stack[-1]=='(' and ch==')':
            stack.pop()
            
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