n, m = map(int, input().split())

result = 0

for i in range(n):
    data = list(map(int, input().split()))
    min_data = min(data)
    print(min_data)
    result = max(result, min_data)
print(result)