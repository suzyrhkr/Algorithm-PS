def binary(i, n):
    answer = ''
    while 0<n:
        answer += str(n%2)
        n //= 2
        
    answer = answer + '0'*(i-len(answer))

    return "".join(list(reversed(answer)))

def solution(n, arr1, arr2):
    final_map = []

    for x, y in zip(arr1, arr2):
        row = ''
        map1 = binary(n, x)
        map2 = binary(n, y)

        for a, b in zip(map1, map2):
    
            if a=='1' or b=='1':
                row += '#'
            else:
                row += ' '
       
        final_map.append(row)

    return final_map

# #---other solution---


def solution(n, arr1, arr2):
    answer = []

    for i,j in zip(arr1, arr2):
        row = str(bin(i|j)[2:])
        row = row.zfill(n)
        row =row.replace('1','#')
        row = row.replace('0',' ')
        answer.append(row)

    return answer
