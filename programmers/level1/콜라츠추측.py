def solution(num):
    answer = 0
    cnt=0

    while num!=1:
        if num%2==0:
            num= num//2
        else:
            num = num*3 + 1
        cnt+=1
        if 500<cnt:
            return -1
    return cnt