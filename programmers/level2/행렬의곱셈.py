def solution(arr1, arr2):
    row = len(arr1)
    col = len(arr2[0])
    answer = [[0]*col for _ in range(row)]

    for i in range(len(arr1)):
        for j in range(len(arr2[0])): 
            for k in range(len(arr2)):
                answer[i][j] += arr1[i][k]*arr2[k][j]
                
    return answer