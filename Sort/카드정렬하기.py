#---시간 초과---

n = int(input())
cards = []
answer = 0

for i in range(n):
    cards.append(int(input()))

cards.sort()

while len(cards)!=1:
    cards.sort()
    a = cards.pop(0)
    b = cards.pop(0)
    answer += a+b
    cards.insert(0, a+b)

print(answer)

#---other solution(using heapq)---

import heapq

n = int(input())
cards = []
answer = 0

for i in range(n):
    heapq.heappush(cards, int(input()))

while len(cards)!=1:
    a = heapq.heappop(cards)
    b = heapq.heappop(cards)

    answer += a+b
    heapq.heappush(cards, a+b)

print(answer)


