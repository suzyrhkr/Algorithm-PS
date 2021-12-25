def solution(s):
    answer = []

    tuple_set = s[2:-2].split('},{')
    tuple_set.sort(key=len)

    for i, t in enumerate(tuple_set):
        t = list(map(int, t.split(",")))
        for ch in t:
            if ch not in answer:
                answer.append(ch)
            
    return answer

