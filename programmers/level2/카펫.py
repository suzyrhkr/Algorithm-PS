def solution(brown, yellow):
    for i in range(1, int(yellow**0.5)+1):
        if yellow/i == int(yellow/i):
            a, b = yellow//i, i

            if brown == 2*(a+b)+4:
                return [a+2, b+2] if b<=a else [b+2, a+2]