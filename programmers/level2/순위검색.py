from bisect import bisect_left
from itertools import combinations
from collections import defaultdict

def solution(infos, querys):
    answer = []
    info_dict = defaultdict(list)
    for info in infos:
        temp = info.split(" ")
        key = temp[:-1]
        score = int(temp[-1])

        for i in range(5):
            for c in list(combinations(key, i)):
                temp_key = ''.join(c)
                info_dict[temp_key].append(score)

    for key in info_dict.keys():
        info_dict[key].sort()

    for query in querys:
        query = query.split(" ")
        query_score = int(query[-1])
        query_key = query[:-1]
        
        selection = ""
        for q in query_key:
            if q not in ['and', '-']:
                selection += q

        if selection in info_dict:
            scoreList = info_dict[selection]
            len_scoreList = len(scoreList)
            if 0 < len_scoreList:
                left, right = 0, len_scoreList
                while left < right:
                    mid = (left + right) // 2
                    if query_score <= scoreList[mid]:
                        right = mid
                    else:
                        left = mid+1
                answer.append(len_scoreList - left)
        else:
            answer.append(0)

    return answer


#---other solution using bisect---
def solution(infos, querys):
    answer = []
    info_dict = defaultdict(list)
    for info in infos:
        temp = info.split(" ")
        key = temp[:-1]
        score = int(temp[-1])

        for i in range(5):
            for c in list(combinations(key, i)):
                temp_key = ''.join(c)
                info_dict[temp_key].append(score)

    for key in info_dict.keys():
        info_dict[key].sort()

    for query in querys:
        query = query.split(" ")
        query_score = int(query[-1])
        query_key = query[:-1]

        selection = ""
        for q in query_key:
            if q not in ['and', '-']:
                selection += q

        if selection in info_dict:
            scoreList = info_dict[selection]
            len_scoreList = len(scoreList)
            if 0 < len_scoreList:
                answer.append(len_scoreList -
                              bisect_left(scoreList, query_score))
        else:
            answer.append(0)

    return answer
