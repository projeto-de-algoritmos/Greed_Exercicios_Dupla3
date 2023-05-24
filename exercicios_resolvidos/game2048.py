q = int(input())
for _ in range(q):
    n = int(input())
    s = sorted(list(map(int, input().split())), reverse=True)
    total = 0
    for num in s:
        if num <= 2048:
            total += num
        if total == 2048:
            break
    print("YES" if total == 2048 else "NO")
