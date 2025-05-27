t,l = map(int, input().split())
arr = [i for i in range(1, t+1)]
for _ in range(l):
    i,j = map(int, input().split())
    arr[i-1:j] = arr[i-1:j][::-1]
print(" ".join(map(str, arr)))
