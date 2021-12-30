def solution(priorities, location):
    answer = 0
    # num, priority
    queue = []
    for i, p in enumerate(priorities):
        queue.append((i,p))

    while queue:
        flag = 0
        num, priority = queue.pop(0)
        
        for x, y in queue:
            if priority < y:
                flag = 1

        if flag == 0:
            answer+=1
            if location == num:
                break
        else:
            queue.append((num, priority))         

    return answer

#---other solution(using function 'any')---

def solution(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    answer = 0

    while True:
        num, priority = queue.pop(0)
        if any(priority < q[1] for q in queue):
            queue.append((num, priority))
        else:
            answer += 1
            if num == location:
                break
    
    return answer