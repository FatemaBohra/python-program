# Question-9
# parameter datatype is list, elements datatype is integer, return datatype is integer
def exchange_first_value_to_last_value(numbers):
    first_value = numbers[0]
    last_value = numbers[len(numbers) - 1]
    numbers[0] = last_value
    numbers[len(numbers) - 1] = first_value
    return numbers

print(exchange_first_value_to_last_value([2, 3, 4, 5, 6]))
