# Question-8
# parameter datatype is list, elements datatype is integer, return datatype is integer
def highest_value(numbers):
    max = numbers[0]
    for i in range(0, len(numbers)):
        if numbers[i] > max:# numbers[1] > numbers[0]
            max = numbers[i]
    return max

print(highest_value([2, 40, 78, 5]))
