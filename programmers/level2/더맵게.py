import heapq

# heapq is faster than sort when using min, max value(iteration)

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while scoville[0]<K:
        first_min_value = heapq.heappop(scoville)
        second_min_value = heapq.heappop(scoville)
        heapq.heappush(scoville, first_min_value+2*second_min_value)
        answer+=1

        if len(scoville)==1 and scoville[0]<K:
            return -1
    
    return answer
