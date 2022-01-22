from bisect import bisect_left, bisect_right

def count_by_range(a, left_value, right_value):
    right = bisect_right(a, right_value)
    left = bisect_left(a, left_value)

    return right-left

def solution(words, queries):
    answer = []

    arr= [[] for _ in range(10001)]
    reversed_arr = [[] for _ in range(10001)]

    for w in words:
        arr[len(w)].append(w)
        reversed_arr[len(w)].append(w[::-1])

    for i in range(10001):
        arr[i].sort()
        reversed_arr[i].sort()

    for q in queries:
        if q[0] != '?':
            cnt = count_by_range(arr[len(q)], q.replace('?','a'), q.replace('?','z'))
        else:
            cnt = count_by_range(reversed_arr[len(q)], q[::-1].replace('?','a'), q[::-1].replace('?','z'))

        answer.append(cnt)

    return answer