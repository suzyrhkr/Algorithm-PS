def solution(s):
    answer = -1
    stack = []

    for ch in s:
        if not stack:
            stack.append(ch)
        elif stack[-1]==ch:
            del stack[-1]
        else:
            stack.append(ch)

    return 1 if not stack else 0
