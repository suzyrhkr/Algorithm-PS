def is_prime_number1(x):
    if x in [0,1]:
        return False
    for i in range(2, int(pow(x, 0.5)) + 1):
        if x % i == 0:
            return False
    return True

# 에라토스테네스의 체
def is_prime_number2(x):
    n = 10000
    arr = [True]*(n+1)
    arr[0], arr[1] = False, False

    for i in range(2, n+1):
        if arr[i] == True:
            for j in range(i*2, n+1, i):
                arr[j] = False

    if arr[x]:
        return True
    else:
        return False

    """
     10000 이하 모든 소수 출력
    for i in range(2, x+1): 
        if arr[i] == True:
            print(i, end=" ")
    """