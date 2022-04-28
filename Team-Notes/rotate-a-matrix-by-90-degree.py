n = 5
space = [[(i*n)+j for j in range(n)] for i in range(n)]

# 1. clockwise 90°
def clockwise_rotate():
    rotated_space = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            rotated_space[j][n - i - 1] = space[i][j]
    return rotated_space

for row in space:
    print(row)
print()

ret = clockwise_rotate()
for row in ret:
    print(row)

'''
space:
[0, 1, 2, 3, 4]
[5, 6, 7, 8, 9]
[10, 11, 12, 13, 14]
[15, 16, 17, 18, 19]
[20, 21, 22, 23, 24]

rotated_space:
[20, 15, 10, 5, 0]
[21, 16, 11, 6, 1]
[22, 17, 12, 7, 2]
[23, 18, 13, 8, 3]
[24, 19, 14, 9, 4]
'''

# 2. clockwise 90°
n, m = 4, 5
space = [[(i*n)+j for j in range(m)] for i in range(n)]

for row in space:
    print(row)
print()

rotated_space = list(map(list, zip(*space[::-1])))

for row in rotated_space:
    print(row)

'''
space:
[0, 1, 2, 3, 4]
[4, 5, 6, 7, 8]
[8, 9, 10, 11, 12]
[12, 13, 14, 15, 16]

rotated_space:
[12, 8, 4, 0]
[13, 9, 5, 1]
[14, 10, 6, 2]
[15, 11, 7, 3]
[16, 12, 8, 4]
'''

# ------------------------------------------------------
n = 5
space = [[(i*n)+j for j in range(n)] for i in range(n)]

# counterclockwise 90°
def counterclockwise_rotate():
    rotated_space = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
             rotated_space[n - j - 1][i] = space[i][j]
    return rotated_space

for row in space:
    print(row)
print()

ret = counterclockwise_rotate()
for row in ret:
    print(row)

'''
space:
[0, 1, 2, 3, 4]
[5, 6, 7, 8, 9]
[10, 11, 12, 13, 14]
[15, 16, 17, 18, 19]
[20, 21, 22, 23, 24]

rotated_space:
[4, 9, 14, 19, 24]
[3, 8, 13, 18, 23]
[2, 7, 12, 17, 22]
[1, 6, 11, 16, 21]
[0, 5, 10, 15, 20]
'''