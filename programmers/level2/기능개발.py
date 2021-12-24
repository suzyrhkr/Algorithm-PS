from math import ceil

def solution(progresses, speeds):
    answer = []
    remain_progresses = []
    days = []
    
    for progress in progresses:
        remain_progresses.append(100-progress)

    for remain_progress, speed in zip(remain_progresses, speeds):
        days.append(ceil((remain_progress/speed)))

    while days:
        count = 1
        day = days.pop(0)

        for i in days:
            if day<i:
                break
            else:
                count += 1
        
        for j in range(count-1):
            days.pop(0)

        answer.append(count)

    return answer