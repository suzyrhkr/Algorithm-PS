#---효율성 테스트 통과 x---
def solution(participant, completion):

    for person in participant:
        try:
            completion.remove(person)
        except:
            return person

  
#---other solution: hash 이용---

def solution(participant, completion):
    answer = ''
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part
        temp += int(hash(part))
    for com in completion:
        temp -= hash(com)
    answer = dic[temp]

    return answer
