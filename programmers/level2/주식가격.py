def solution(prices):
    answer = []
    
    for i in range(len(prices)-1):
        j = i
        cnt = 0

        while j<len(prices)-1 and prices[i]<=prices[j]:
            j += 1
            cnt += 1
        answer.append(cnt)

    answer.append(0)

    return answer
