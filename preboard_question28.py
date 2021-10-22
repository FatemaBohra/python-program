
# parameter datatype list, return datatype list
# sub prob 1 - accept two list, ARR and Detail
# sub prob 2 - insert first five values of detail in ARR
def push_stack(arr, detail, third):
    for i in range(0, 6):
         arr.append(detail[i])
    for i in range(- 1, -4, -1):
         print(third[i])
         arr.append(third[i])
    return arr


# arr_global = int(input('enter a list'))
# detail_global = int()

print(push_stack([1, 2, 3, 4], [5, 6, 78, 89, 2, 6, 8], [4, 5, 6, 7, 8, 9]))
