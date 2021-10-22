# Question-1(STACKS AND QUEUES)
# parameter datatype list, element datatype is integer, return datatype integer
def pop(arr_stack):
    if len(arr_stack) == 0:
        return 'stack is empty'
    else:
        deleted_value = arr_stack.pop()#
        return deleted_value

arr_stack_global = list() # created an empty stack
arr_stack_global.append(1)
arr_stack_global.append(2)
arr_stack_global.append(3)

print(pop(arr_stack_global))