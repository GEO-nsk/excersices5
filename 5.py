def mod_number(a,b):
    if a < b:
        return a
    else:
        return mod_number(a - b,b)

a = int(input())
b = int(input())

print(mod_number(a,b))