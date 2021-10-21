# Q- 6 write a function which prints sum of even values from the odd location of a list
# parameter datatype is list, elements datatype is integer, return datatype is integer
def my_function(numbers):
    sum = 0
    for i in range(0, len(numbers)): # range = 0-3, i = 0, i = 1, i = 2, i = 3
        if i % 2 != 0 and numbers[i] % 2 == 0:
            sum = sum + numbers[i]
    return sum

print(my_function([2, 4, 6, 8]))
