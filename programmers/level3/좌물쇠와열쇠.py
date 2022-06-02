def rotate(space):
    rotated_space = list(map(list, zip(*space[::-1])))
    return rotated_space

def check(lock):
    lock_length = len(lock) // 3
    for i in range(lock_length, lock_length*2):
        for j in range(lock_length, lock_length*2):
            if lock[i][j] != 1:
                return False
    return True

def solution(key, lock):
    n = len(lock)
    m = len(key)
    new_lock = [[0]*(n*3) for _ in range(n*3)]
    for i in range(n):
        for j in range(n):
            new_lock[n+i][n+j] = lock[i][j]

    for rotation in range(4):
        key = rotate(key)
        for x in range(n*2):
            for y in range(n*2):
                # 열쇠 끼우기
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] += key[i][j]

                if check(new_lock):
                    return True
                # 열쇠 빼기
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] -= key[i][j]
    return False