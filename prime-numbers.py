def is_prime(n):
    if n < 2:
        return False
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True


# numbers = open('numbers.txt').read().split('\n')
# numbers = list(map(int, numbers))
# for number in numbers:
#     print(number, end=" ")
#     if is_prime(number):
#         print("Liczba pierwsza")
#     else:
#         print()

for number in range(1, 101):
    print(number, end=" ")
    if is_prime(number):
        print("Liczba pierwsza")
    else:
        print()
