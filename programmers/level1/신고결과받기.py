def solution(id_list, report, k):
    answer = []
    reports = {}
    reported = []
    suspended = {}

    for line in set(report):
        user_id, reported_id = line.split(' ')
        reported.append(reported_id)
        
        if user_id in reports:
            contents = reports[user_id]
            contents.append(reported_id)
            reports[user_id] = contents
        else:
            reports[user_id] = [reported_id]

    for user_id in id_list:
        cnt = reported.count(user_id)
        if k <= cnt:
            suspended[user_id] = cnt

    for user_id in id_list:
        cnt_id = 0
        if user_id in reports:
            for id_ in reports[user_id]:
                if id_ in suspended:
                    cnt_id += 1
        else:
            cnt_id = 0

        answer.append(cnt_id)           
    return answer

#---other solution---
def solution(id_list, report, k):
    answer = [0] * len(id_list)    
    reports = {x : 0 for x in id_list}

    for r in set(report):
        reports[r.split()[1]] += 1

    for r in set(report):
        if reports[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] += 1

    return answer