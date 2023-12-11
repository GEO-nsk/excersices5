def count(n):
    if n == 1:
        return 1
    else:
        return 1 + count(n // 10)

n = int(input())

print(count(n))