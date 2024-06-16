a = 9
b = 15
print(f"Liczby: {a} i {b}")
while a != b:
    if a > b:
        a = a - b
    else:
        b = b - a
print(f"NWD: {a}")