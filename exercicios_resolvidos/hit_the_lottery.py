def min_bills(n):
    denominations = [100, 20, 10, 5, 1]
    count = 0
    for denom in denominations:
        count += n // denom
        n %= denom
    return count

n = int(input().strip())
print(min_bills(n))
