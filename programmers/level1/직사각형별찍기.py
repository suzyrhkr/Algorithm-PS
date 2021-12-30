a, b = map(int, input().strip().split(' '))

for i in range(b):
    for j in range(a):
        print('*',end="")
    print()

#---other solution---

a, b = map(int, input().strip().split(' '))
print(("*" * a + "\n") * b)

