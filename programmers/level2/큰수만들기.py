def solution(number, k):
    answer = ''
    stack = []
    
    for n in number:
        while stack and k and stack[-1]<n:
            del stack[-1]
            k-=1
            
        stack.append(n)
        
    stack = "".join(stack).lstrip("0")

    return stack[:len(stack)-k]