# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)
#
#
# for i in range(35):
#     print(fibonacci(i), end=" ")
fibonacci_list = []
for i in range(135):
    if i == 0 or i == 1:
        fibonacci_list.append(i)
    else:
        fibonacci_list.append(fibonacci_list[-1] + fibonacci_list[-2])
print(fibonacci_list)
