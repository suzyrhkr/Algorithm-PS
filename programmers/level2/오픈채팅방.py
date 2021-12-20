def solution(record):
    answer = []
    user_info = {}

    for sentence in record:
        st = sentence.split(' ')
        
        if st[0]=='Enter' or st[0]=='Change':
            uid, name = st[1], st[2]
            user_info[uid] = name
    
    for sentence in record:
        st = sentence.split(' ')

        if st[0]=='Enter':
            answer.append("{}님이 들어왔습니다.".format(user_info[st[1]]))
        
        elif st[0]=='Leave':
            answer.append("{}님이 나갔습니다.".format(user_info[st[1]]))
    return answer