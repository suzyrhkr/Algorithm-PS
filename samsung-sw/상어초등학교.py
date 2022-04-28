# get input
n = int(input())
students_info = []
seats = [[0]*n for _ in range(n)]

for _ in range(pow(n,2)):
    line = list(map(int, input().split()))
    students_info.append((line[0], line[1:]))

# up, down, left, right
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# def
def findRowCol(seats, st, n):
    r,c = -1, -1
    for row in range(n):
        for col in range(n):
            if seats[row][col] == st:
                r, c = row, col 
    if r==c==-1:
        return False
    return r, c

def n_AdjacentEmptySeats(seats, r, c):
    cnt = 0
    empty_seats = []

    for x, y in zip(dx, dy):
        if  n <= r+x or r+x < 0 or n <= c+y or c+y < 0:
            continue
        if seats[r+x][c+y] == 0:
            empty_seats.append((r+x, c+y))
            cnt += 1
    return cnt, empty_seats

def n_favoriteStudents(seats, r, c, f_sts):
    cnt = 0

    for x, y in zip(dx, dy):
        if  n <= r+x or r+x < 0 or n <= c+y or c+y < 0:
            continue
        if seats[r+x][c+y] in f_sts:
            cnt += 1
    return cnt

def getScore(students_info, seats):
    score = 0
    
    for st, f_sts in students_info:
        cnt = 0
        r, c = findRowCol(seats, st, n)
        for x, y in zip(dx, dy):
            if  n <= r+x or r+x < 0 or n <= c+y or c+y < 0:
                continue
            if seats[r+x][c+y] in f_sts:
                cnt += 1
        if 0<cnt:
            score += 10**(cnt-1)
    return score

# main code
for st, f_sts in students_info:
    tmp_seats = []
    if st == students_info[0][0]:
        seats[1][1] = st
        continue

    # condition 1
    first_tmp = {}
    for i in range(n):
        for j in range(n):
            if seats[i][j] != 0:
                continue
            cnt = n_favoriteStudents(seats, i, j, f_sts)
            first_tmp[(i, j)] = cnt
    tmp = [k for k,v in first_tmp.items() if max(first_tmp.values()) == v]

    if len(tmp) == 1:
        s_x, s_y = tmp[0][0], tmp[0][1]
        seats[s_x][s_y] = st
        continue

    # condition 2
    second_tmp = {}
    for row, col in tmp:
        cnt, _ = n_AdjacentEmptySeats(seats, row, col)
        second_tmp[(row, col)] = cnt
    tmp = [k for k,v in second_tmp.items() if max(second_tmp.values()) == v]

    if len(tmp) == 1:
        s_x, s_y = tmp[0][0], tmp[0][1]
        seats[s_x][s_y] = st
        continue

    # condition 3
    tmp.sort(key=lambda x: (x[0],x[1]))
    s_x, s_y = tmp[0]
    seats[s_x][s_y] = st
    
score = getScore(students_info, seats)
print(score)

#---other solution---
# sort 함수 key = lambda를 이용하여 한 번에 정렬한 풀이
# 1' 00
import sys

input = sys.stdin.readline
n = int(input())
info = [list(map(int, input().split())) for _ in range(n*n)]
space = [[0]*n for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def calculate_score():
    score = 0
    for i in range(n):
        for j in range(n):
            for k in range(n**2):
                if space[i][j] == info[k][0]:
                    favorite = info[k][1:]
                    break
            cnt = 0
            for idx in range(4):
                nx, ny = i + dx[idx], j + dy[idx]
                if 0 <= nx and nx < n and 0 <= ny and ny < n:
                    if space[nx][ny] in favorite:
                        cnt += 1
            if cnt == 0:
                score += 0
            else:
                score += 10**(cnt-1)
    return score

def find_space(favorite):
    arr = []
    for i in range(n):
        for j in range(n):
            favorite_cnt, void_cnt = 0, 0
            if 0 < space[i][j]:  # 이미 자리를 정한 학생이 있는 경우
                continue
            for idx in range(4): # 현재 위치에서 4 방향 탐색
                nx, ny = i + dx[idx], j + dy[idx]
                if 0 <= nx and nx < n and 0 <= ny and ny < n:
                    if space[nx][ny] == 0: # 비어있는 칸
                        void_cnt += 1
                    else: # 비어있지 않은 경우
                        if space[nx][ny] in favorite: # 지금 칸에 있는 학생이 좋아하는 학생일 경우
                            favorite_cnt += 1
            arr.append([favorite_cnt, void_cnt, i, j]) # 좋아하는 학생 수 / 비어있는 칸 수
    return arr

for i, x in enumerate(info):
    st = x[0]
    favorite = [x[1], x[2], x[3], x[4]]

    arr = find_space(favorite) 
    arr.sort(key=lambda x:(-x[0], -x[1], x[2], x[3]))
    st_x, st_y = arr[0][2], arr[0][3]

    space[st_x][st_y] = st # 자리 배치

print(calculate_score())

"""
상어 초등학교

학생: 1~n**2번 
인접 조건: 상하좌우

1. 비어있는 칸 중 좋아하는 학생과 인접한 칸이 가장 많은 칸
2. 1이 여러 개이면, 좋아하는 학생과 인접한 칸 중에서 비어있는 칸이 가장 많은 칸
3. 2도 여러 개이면, 행, 열 번호 작은 칸 

output: 자리 배치 후 만족도(좋아하는 학생 수에 따라 결정)의 총합
"""