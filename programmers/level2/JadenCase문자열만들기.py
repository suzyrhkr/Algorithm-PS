def solution(s):
    answer = ''
    words = s.split(' ')
    
    for w in words:
        if not w:
            answer += ' '
            continue
            
        answer += w[0].upper() + w[1:].lower()
        answer += ' '
        
    return answer[:-1]