'''combinations'''
def combination(arr, n):
    result = []
    if n == 0:
        return [[]]
    for i in range(len(arr)):
        elem = arr[i]
        for rest in combination(arr[i + 1:], n - 1):
            result.append([elem] + rest)
    return result
print(combination(['A','A','B'], 2))
# [['A', 'A'], ['A', 'B'], ['A', 'B']]

'''permutations'''
def permutation(arr, n):
    result = []
    if n == 0:
        return [[]]
    for i in range(len(arr)):
        elem = arr[i]
        for rest in permutation(arr[:i] + arr[i+1:], n - 1):
            result.append([elem] + rest)
    return result
print(permutation(['A','A','B'], 2))
# [['A', 'A'], ['A', 'B'], ['A', 'A'], ['A', 'B'], ['B', 'A'], ['B', 'A']]