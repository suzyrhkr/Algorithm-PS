class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        answer = 0
        while True:
            if not stones:
                answer = 0
            if len(stones) == 1:
                answer = stones[0]
                break
            
            stones.sort()
            first = stones.pop()
            second = stones.pop()
            stones.append(abs(first-second))
            
        return answer 
        
        