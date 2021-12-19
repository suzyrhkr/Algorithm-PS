def solution(lottos, win_nums):
    answer = []
    count = 0
    count_zero = lottos.count(0)

    # 당첨:순위
    awards = {0:6, 1:6, 2:5, 3:4, 4:3, 5:2, 6:1}

    for num in lottos:
        if num in win_nums:
            count+=1
    
    highest = count_zero + count
    lowest = count

    answer.append(awards[highest])
    answer.append(awards[lowest])
    return answer