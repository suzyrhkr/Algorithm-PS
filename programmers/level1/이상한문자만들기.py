def solution(s):
    answer = []
    
    for word in s.split(' '):
        result = ''
        for i, ch in enumerate(word):
            result += ch.upper() if i%2==0 else ch.lower()
        answer.append(result)

    return ' '.join(answer)