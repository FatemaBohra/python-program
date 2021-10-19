# Question-7(STACK AND QUEUE)
def add_element(data, x):
    data.append(x)
    return data

def delete_element(data, index):
    if len(data) == 0:
        return 'queue is empty'
    elif len(data) - 1 < index:
        return 'overflow'
    else:
        deleted_value = data.pop(index)
        return deleted_value

data_global = []
a = int(input('enter an element'))
print(add_element(data_global, a))
b = int(input('enter an index'))
print(delete_element(data_global, b))


