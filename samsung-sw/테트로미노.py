import sys

input = sys.stdin.readline
n, m = map(int, input().split())
space = [list(map(int, input().split())) for _ in range(n)]

shape = []
shape_1_1 = [(0,0), (0,1), (0,2), (0,3)]
shape_1_2 = [(0,0), (1,0), (2,0), (3,0)]

shape_2_1 = [(0,0), (0,1), (1,0), (1,1)]

shape_3_1 = [(0,0), (1,0), (2,0), (2,1)]
shape_3_2 = [(0,1), (1,1), (2,1), (2,0)]
shape_3_3 = [(0,0), (1,0), (2,0), (0,1)]
shape_3_4 = [(0,0), (0,1), (1,1), (2,1)]
shape_3_5 = [(0,0), (1,0), (1,1), (1,2)]
shape_3_6 = [(0,2), (1,0), (1,1), (1,2)]
shape_3_7 = [(0,0), (0,1), (0,2), (1,0)]
shape_3_8 = [(0,0), (0,1), (0,2), (1,2)]

shape_4_1 = [(0,0), (0,1), (0,2), (1,1)]
shape_4_2 = [(0,1), (1,0), (1,1), (1,2)]
shape_4_3 = [(0,0), (1,0), (2,0), (1,1)]
shape_4_4 = [(0,1), (1,1), (2,1), (1,0)]

shape_5_1 = [(0,0), (1,0), (1,1), (2,1)]
shape_5_2 = [(0,1), (1,0), (1,1), (2,0)]
shape_5_3 = [(0,1), (0,2), (1,0), (1,1)]
shape_5_4 = [(0,0), (0,1), (1,1), (1,2)]

shape = [shape_1_1, shape_1_2, shape_2_1,
         shape_3_1, shape_3_2, shape_3_3, shape_3_4, shape_3_5, shape_3_6, shape_3_7, shape_3_8,
         shape_4_1, shape_4_2, shape_4_3, shape_4_4,
         shape_5_1, shape_5_2, shape_5_3, shape_5_4]

max_value = float('-inf')

for sh in shape:

    for i in range(n):
        for j in range(m):
            total = 0
            # 벗어나지 않는지 체크
            for x, y in sh:
                nx, ny = i + x, j + y
                if nx < 0 or n <= nx or ny < 0 or m <= ny:
                    break
            else:
                for x, y in sh:
                    nx, ny = i + x, j + y
                    total += space[nx][ny]
                max_value = max(max_value, total)

print(max_value)



