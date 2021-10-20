# 1- wap to take 5 elements if even print cube else print sq
def cube_or_square(numbers):
    for i in range(0, len(numbers)):
        if numbers[i] % 2 == 0:
            print(numbers[i] ** 3)
        else:
            print(numbers[i] ** 2)

cube_or_square([2, 4, 6, 3, 8])

# 2- wap to find out how many times 7 is occurring in list
# parameter datatype is list, elements/values datatype is integer, return datatype is integer
def occurrence_of_7(numbers):
    count = 0
    for i in range(0, len(numbers)): # range = 0-4, i = 0, i = 1, i = 2, i = 3, i = 4
        if numbers[i] == 7: # numbers[4] = 7
            count = count + 1 # count = 1 + 1 = 2
    return count # 2

print(occurrence_of_7([4, 5, 7, 8, 7]))

