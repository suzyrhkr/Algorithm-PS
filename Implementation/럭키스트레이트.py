n = input()

mid = len(n) // 2
head = n[:mid]
tail = n[mid:]

sum_head, sum_tail = 0, 0
for i in range(mid):
    sum_head += int(head[i])
    sum_tail += int(tail[i])

if sum_head == sum_tail:
    print('LUCKY')
else:
    print("READY")
