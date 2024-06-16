def avg_list(list_number):
    sum = 0
    for i in list_number:
        sum += i
    return sum / len(list_number)


# my_list = [4, 6, 7, 12, 9]
# print(avg_list(my_list))

numbers = open('numbers.txt').read().split('\n')
numbers = list(map(int, numbers))
print(avg_list(numbers))
