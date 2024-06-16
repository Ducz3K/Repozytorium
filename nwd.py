pairs = open('nwd.txt').read().split('\n')
# print(pairs)
for pair in pairs:
    numbers = pair.split(' ')
    numbers = list(map(int, numbers))
    print(numbers, end=" ")
    while numbers[0] != numbers[1]:
        if numbers[0] > numbers[1]:
            numbers[0] = numbers[0] - numbers[1]
        else:
            numbers[1] = numbers[1] - numbers[0]
    print(f"NWD: {numbers[0]}")
