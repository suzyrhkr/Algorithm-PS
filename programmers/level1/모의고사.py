def solution(answers):
    answer=[]
    a_cnt, b_cnt, c_cnt = 0, 0, 0

    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    a_answer = a*(len(answers)//len(a)) + a[:len(answers)%len(a)]
    b_answer = b*(len(answers)//len(b)) + b[:len(answers)%len(b)]
    c_answer = c*(len(answers)//len(c)) + c[:len(answers)%len(c)]
    
    for x, y, z, ans in zip(a_answer, b_answer, c_answer, answers):
        if x==ans :
            a_cnt+=1
        if y==ans :
            b_cnt+=1
        if z==ans:
            c_cnt+=1

    cnt = {1:a_cnt, 2:b_cnt, 3:c_cnt}

    for key, value in cnt.items():
        if max(cnt.values()) == value:
            answer.append(key)

    return answer.sort()