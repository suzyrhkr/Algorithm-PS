import sys
from collections import deque

n = int(input())
info = deque()
for _ in range(n):
    t, x, y = map(int, input().split())
    info.append([t, x, y])

space = [[False for _ in range(10)] for _ in range(10)]
score = 0

def count_block():
    cnt = 0
    for i in range(0,4):
        for j in range(6,10):
            if space[i][j]:
                cnt += 1
            if space[j][i]:
                cnt += 1
    return cnt

def move(t, x, y):
    bx, by = x, y
    if t == 1:
        # 초록색 처리
        while (bx + 1 < 10 and not space[bx+1][by]):
            bx += 1
        space[bx][by] = True
        # 파란색 처리
        bx, by = x, y
        while (by + 1 < 10 and not space[bx][by+1]):
            by += 1
        space[bx][by] = True
    elif t == 2:
        # 초록색 처리
        while (bx + 1 < 10 and not space[bx+1][by] and not space[bx+1][by+1]):
            bx += 1
        space[bx][by], space[bx][by+1] = True, True
        # 파란색 처리
        bx, by = x, y
        while (by + 2 < 10 and not space[bx][by+1] and not space[bx][by+2]):
            by += 1
        space[bx][by], space[bx][by+1] = True, True
    elif t == 3:
        # 초록색 처리
        while (bx + 2 < 10 and not space[bx+1][by] and not space[bx+2][by]):
            bx += 1
        space[bx][by], space[bx+1][by] = True, True
        # 파란색 처리
        bx, by = x, y
        while (by + 1 < 10 and not space [bx][by+1] and not space[bx+1][by+1]):
            by += 1
        space[bx][by], space[bx+1][by] = True, True

def remove():
    # 초록색 처리
    score = 0
    for i in range(6, 10):
        cnt = 0
        for j in range(0, 4):
            if space[i][j]:
                cnt += 1
        if cnt == 4:
            score += 1
            del space[i]
            space.insert(4, [False]*10)
    # 파란색 처리
    for j in range(6, 10):
        cnt = 0
        for i in range(0, 4):
            if space[i][j]:
                cnt += 1
        if cnt == 4:
            score += 1
            for k in range(4):
                space[k][j] = False
            for y in range(j-1, 3, -1):
                for x in range(4):
                    space[x][y+1] = space[x][y]
    return score

def remove2():
    # 초록색 처리
    cnt = 0
    for i in range(4, 6):
        for j in range(0, 4):
            if space[i][j]:
                cnt += 1
                break
    for _ in range(cnt):
        del space[-1]
        space.insert(4, [False]*10)
    # 파란색 처리
    cnt = 0
    for j in range(4, 6):
        for i in range(0, 4):
            if space[i][j]:
                cnt += 1
                break
    for _ in range(cnt):
        for i in range(0, 4):
            del space[i][-1]
            space[i].insert(4, False)

for _ in range(n):
    t, x, y = info.popleft()
    move(t, x, y)
    ret = remove()
    score += ret
    remove2()

print(score)
print(count_block())