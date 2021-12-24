import re

def solution(new_id):
    answer = ''
    # 1
    new_id = new_id.lower()
    # 2
    for c in new_id:
        if c.isalpha() or c.isdigit() or c in ['-', '_', '.']:
            answer += c
    # 3
    while '..' in answer:
        answer = answer.replace('..', '.')
    # 4
    if answer and answer[0]=='.':
        answer = answer[1:]
  
    if answer and answer[-1]=='.':
        answer = answer[:-1]
    # 5 
    if not answer:
        answer = 'a'
    # 6
    if 16<=len(answer):
        answer = answer[:15]
        if answer[-1]=='.':
            answer = answer[:-1]
    # 7
    if len(answer)<=2:
        while len(answer)<3:
            answer += answer[-1]

    return answer

#---other solution: re 정규식---

def solution(new_id):
    st = new_id
    st = st.lower()
    st = re.sub('[^a-z0-9\-_.]', '', st)
    st = re.sub('\.+', '.', st)
    st = re.sub('^[.]|[.]$', '', st)
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st)
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
    return st
