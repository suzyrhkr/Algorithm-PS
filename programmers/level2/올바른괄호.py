def solution(s):
    answer = True
    s = list(s)
    stack = []
    
    if not s or s[0] == ')':
        return False
                
    for ch in s:
        if ch == '(':
            stack.append(ch)
        else:
            if not stack:
                answer = False
                break
            if stack[-1] == '(':
                del stack[-1]
                
    if stack:
        answer = False

    return answer