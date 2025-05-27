arr = []
for _ in range(10):
    val = int(input()) % 42
    if val not in arr:
        arr.append(val)
print(len(arr))
