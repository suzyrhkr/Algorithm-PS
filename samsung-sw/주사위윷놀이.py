import sys

input = sys.stdin.readline
dice = list(map(int, input().split()))

space = [list(range(0,41,2)), # 0번 road
          [10, 13, 16, 19, 25, 30, 35, 40], # 1번 road
          [20, 22, 24, 25, 30, 35, 40], # 2번 road
          [30, 28, 27, 26, 25, 30, 35, 40]] # 3번 road

horse = [[0, 0], [0, 0], [0, 0], [0, 0]] # road에서의 index / road index
max_score = 0

def game(n, score, horse):
    global max_score
    if 10 <= n: # 종료 조건
        max_score = max(max_score, score)
        return

    # 완전 탐색
    for h in range(4):
        if horse[h][0] == -1: # 말이 도착 칸에 있는 경우
            continue
        curr = [horse[h][0] + dice[n], horse[h][1]] # 주사위 수만큼 이동할 칸의 정보
        if curr[1] == 0: # 0번 road인 경우, 분기점에 도착했을 때 처리
            if curr[0] == 5: # 점수 10인 칸
                curr[1] = 1
                curr[0] = 0
            elif curr[0] == 10: # 점수 20인 칸
                curr[1] = 2
                curr[0] = 0
            elif curr[0] == 15: # 점수 30인 칸
                curr[1] = 3
                curr[0] = 0

        if len(space[curr[1]]) <= curr[0]: # 이동할 칸이 도착 지점이거나 넘어서는 경우
            curr[0] = -1 # 도착 체크
            tmp = horse[h] 
            horse[h] = curr
            game(n+1, score, horse) # back tracking
            horse[h] = tmp # back tracking 후 undo

        else: # 도착지점이 아닌 곳에 다른 말이 없을 경우 -> 탐색
            curr_score = space[curr[1]][curr[0]]
            flag = False
            for i in range(4):
                if horse[i][0] == -1: # 말이 도착지점에 있는 경우
                    continue
                # ** 점수가 같은 경우 처리
                if h != i and curr_score == space[horse[i][1]][horse[i][0]]: 
                    if curr_score == 30: # 점수 30인 경우 처리
                        if curr == [0, 3] and horse[i] in [0, 3]:
                            flag = True
                            break
                        elif curr != [0, 3] and horse[i] != [0, 3]:
                            flag = True
                            break
                    elif curr_score in [16, 22, 24, 26, 28]:
                        if curr == horse[i]:
                            flag= True
                            break
                    else:
                        flag = True
                        break

            if flag: # 이동할 칸에 이미 다른 말이 있는 경우 -> 탐색 종료
                continue

            tmp = horse[h]
            horse[h] = curr
            game(n+1, score + space[curr[1]][curr[0]], horse) # back tracking
            horse[h] = tmp # back tracking 후 undo

game(0, 0, horse)
print(max_score)