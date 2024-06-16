numbers = open('numbers.txt').read().split('\n')
numbers = list(map(int, numbers))
print(numbers)
# for number in numbers:
#     if number % 2 == 0:
#         print(f"{number}\tparzysta")
#     else:
#         print(f"{number}\tnieparzysta")
numbers.sort()
print(numbers)
sum = 0
for number in numbers:
    sum += number
avg = sum / len(numbers)
print(f"Średnia: {avg}, Minimum: {numbers[0]}, Maksimum: {numbers[-1]}")
