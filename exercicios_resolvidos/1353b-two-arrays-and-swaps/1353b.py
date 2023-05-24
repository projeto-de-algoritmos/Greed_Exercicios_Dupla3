t = int(input())

while t > 0:
    inp = input().split(' ')
    n = int(inp[0])
    k = int(inp[1])

    a = input().split(' ')
    a = [int(number) for number in a]

    b = input().split(' ')
    b = [int(number) for number in b]

    a.sort()
    b.sort(reverse=True)

    while k > 0 and a[0] < b[0]:
        temp = a[0]
        a[0] = b[0]
        b[0] = temp
        
        a.sort()
        b.sort(reverse=True)
        
        k -= 1

    sum_a = 0
    for number in a:
        sum_a += int(number)

    print(str(sum_a))

    t -= 1
