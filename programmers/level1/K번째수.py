def solution(array, commands):
    answer = []
    for i, command in enumerate(commands):
        i, j, k = command
        answer.append(sorted(array[i-1:j])[k-1])
    return answer