import sys
from collections import deque

input = sys.stdin.readline
n, k = map(int, input().split())
belt = list(map(int, input().split()))
robot_belt = []
for i in range(2*n):
    robot_belt.append([[], belt[i]]) # 로봇 올라간 순서대로 번호 1,2, ... / 내구도
robot_belt = deque(robot_belt)

robot_idx = 0
def process():
    global robot_idx
    # 1. 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전
    robot_belt.insert(0, robot_belt.pop())
    robot_belt[n-1][0] = [] # 이동 후 내리는 곳에 로봇 모두 내리기
    # 2. 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동
    recent_robot = []
    for i in range(2*n):
        if robot_belt[i][0]:
            for j in robot_belt[i][0]:
                recent_robot.append((j, i))
    recent_robot.sort(key=lambda x: x[0])

    for robot, pos in recent_robot:
        if  2*n == pos+1:
            new_pos = 0
        else:
            new_pos = pos+1
        if 0 < robot_belt[new_pos][1] and not robot_belt[new_pos][0]:
            if new_pos != n-1:
                robot_belt[new_pos][0].append(robot)
            robot_belt[new_pos][1] -= 1
            robot_belt[pos][0].remove(robot)

    # 3. 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올림
    if 0 < robot_belt[0][1]:
        robot_belt[0][0].append(robot_idx)
        robot_idx += 1 
        robot_belt[0][1] -= 1

idx = 1
while True:
    process()
    cnt = 0
    for r in robot_belt:
        if r[1] == 0:
            cnt += 1
    # 4. 내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료
    if k <= cnt:
        break
    idx += 1

print(idx)
