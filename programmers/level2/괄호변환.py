# 올바른 문자열 체크 함수
def check_right_str(s):
    stack = []
    for ch in s:
        if ch == '(':
            stack.append(ch)
        else:
            if stack and stack[-1] == '(':
                del stack[-1]
                continue
            elif not stack:
                stack.append(ch)
                
    return True if not stack else False

def uv_split(w):
    cnt1, cnt2 = 0, 0
    ret_s = ""
    flag = False
    u, v = "", ""
    for i, ch in enumerate(w):
        if (cnt1 != 0 and cnt2 != 0) and cnt1 == cnt2:
            flag = True
        if not flag:
            u += ch
            if ch == '(': cnt1 += 1
            else: cnt2 += 1
        else:
            v = w[i:]
            break            
    return u, v
    
    
def recursion(s):
    if s == "":
        return s
    # w를 u, v로 분리
    u, v = uv_split(s)
    
    if check_right_str(u):
        ret = recursion(v)
        return u + ret
        # 수행한 결과 문자열을 u에 이어 붙인 후 반환
        
    else:
        new_s = "("
        ret = recursion(v) # 수행 결과 문자열 이어 붙임
        new_s += ret
        new_s += ")"
        
        for ch in u[1:-1]:
            if ch == '(':
                new_s += ')'
            else:
                new_s += '('    
    return new_s

def solution(p):
    answer = ''
    if check_right_str(p):
        return p
    answer = recursion(p)
    
    return answer