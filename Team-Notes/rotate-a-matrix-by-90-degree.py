# n*m matrix

n, m = 4, 5
space = [[(i*n)+j for j in range(m)] for i in range(n)]

# 1. clockwise 90°
def clockwise_rotate():
    rotated_space = [[0]*n for _ in range(m)]
    for i in range(n):
        for j in range(m):
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
n, m = 4, 5
space = [[(i*n)+j for j in range(m)] for i in range(n)]

# counterclockwise 90°
def counterclockwise_rotate():
    rotated_space = [[0]*n for _ in range(m)]
    for i in range(n):
        for j in range(m):
             rotated_space[m - j - 1][i] = space[i][j]
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
[4, 5, 6, 7, 8]
[8, 9, 10, 11, 12]
[12, 13, 14, 15, 16]

rotated_space:
[4, 8, 12, 16]
[3, 7, 11, 15]
[2, 6, 10, 14]
[1, 5, 9, 13]
[0, 4, 8, 12]
'''