# Question-8(stack and queue)
def add_element(data, x):
    data.append(x)
    return data

def display_element(data, index):
    if len(data) == 0:
        return 'stack is empty'
    elif index > len(data) - 1:
        return 'overflow'
    else:
        return data[index]

data_global = list()

a = int(input('enter an element'))
print(add_element(data_global, a))

b = int(input('enter an index'))
print(display_element(data_global, b))