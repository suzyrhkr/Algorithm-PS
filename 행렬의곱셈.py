def solution(arr1, arr2):
    len_arr1 = len(arr1)
    answer = [[0]*len(arr2[0]) for _ in range(len_arr1)]
    
    for i in range(len_arr1):
        for j in range(len(arr2[0])):
            for k in range(len(arr2)):
                answer[i][j] += arr1[i][k] * arr2[k][j]
    
    return answer