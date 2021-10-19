# Question-4(STACK AND QUEUE)
# parameter data is list, element data is integer, return data is integer
def insertQ(arr, data):
    arr.append(data)
    return arr

def delete(arr):
    if len(arr) == 0:
        return 'queue is empty'
    else:
        deleted_value = arr.pop(0)
        return deleted_value

arr_global = []

print(insertQ(arr_global, 23))
print(insertQ(arr_global, 12))

print(delete(arr_global))


