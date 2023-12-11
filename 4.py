def sum_progress(a1, r, n):

    if n == 1:
        return a1
    else:
        return a1 + sum_progress(a1 + r, r, n - 1)

a1 = int(input())
r = int(input())
n = int(input())

print(sum_progress(a1, r, n))