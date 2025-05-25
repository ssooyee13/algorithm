stu = [i for i in range(1, 31)]
for _ in range(28):
    val = int(input())
    stu.remove(val)
print(f"{min(stu)}\n{max(stu)}")
