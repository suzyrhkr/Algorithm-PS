def solution(s, n):
    answer = ''

    for ch in s:
        if ch == ' ':
            answer += ch
        elif ch.isupper():
            if ord('Z') < ord(ch)+n:
                answer += chr(ord(ch)+n-26)
            else:
                answer += chr(ord(ch)+n)
        elif ch.islower():
            if ord('z') < ord(ch)+n:
                answer += chr(ord(ch)+n-26)
            else:
                answer += chr(ord(ch)+n)
        
    return answer

#---other solution---

def solution(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i]=chr((ord(s[i])-ord('A')+ n)%26+ord('A'))
        elif s[i].islower():
            s[i]=chr((ord(s[i])-ord('a')+ n)%26+ord('a'))

    return "".join(s)