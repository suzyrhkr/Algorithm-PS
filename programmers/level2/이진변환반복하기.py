def binary_transformation(s):
    n_one = s.count('1')
    ret_s = str(bin(n_one)[2:])
    return ret_s, len(s)-n_one

def solution(s):
    answer = []
    cnt = 0
    cnt_zero = 0

    while s != '1':
        s, ret = binary_transformation(s)
        cnt_zero += ret
        cnt += 1
        
    return [cnt, cnt_zero]