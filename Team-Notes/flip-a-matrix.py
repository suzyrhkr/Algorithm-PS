n = 5
space = [[(i*n)+j for j in range(n)] for i in range(n)]
for row in space:
    print(row)
print()

flipped_space = list(map(list, zip(*space)))
for row in flipped_space:
    print(row)

'''
space:
[0, 1, 2, 3, 4]
[5, 6, 7, 8, 9]
[10, 11, 12, 13, 14]
[15, 16, 17, 18, 19]
[20, 21, 22, 23, 24]

flipped_space:
[0, 5, 10, 15, 20]
[1, 6, 11, 16, 21]
[2, 7, 12, 17, 22]
[3, 8, 13, 18, 23]
[4, 9, 14, 19, 24]
'''
