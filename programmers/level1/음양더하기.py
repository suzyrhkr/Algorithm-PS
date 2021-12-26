def solution(absolutes, signs):
    answer = 0

    for abs, sign in zip(absolutes, signs):
        answer += abs if sign==True else -abs

    return answer