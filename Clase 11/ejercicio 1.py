def promedio_variable(*args):
    total = 0
    for num in args:
        total += num
    return total / len(args)

print(promedio_variable(10, 20, 30))        # 20.0
print(promedio_variable(5, 15, 25, 35))     # 20.0
