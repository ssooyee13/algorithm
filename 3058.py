t = int(input())
for _ in range(t):
    result = []
    arr = list(map(int, input().split()))
    for i in arr:
        if i % 2 == 0:
            result.append(i)
    print(sum(result), min(result))
    
