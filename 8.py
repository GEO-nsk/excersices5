def fib(k):
    if k < 3:
        return 1
    else:
        return fib(k-1) + fib(k-2)

k = int(input())

print(fib(k))