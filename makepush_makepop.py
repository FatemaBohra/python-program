# Question-5(STACK AND QUEUE)
def makepush(package, x):
    package.append(x) # insert rear
    return package

def makepop(package):
    if len(package) == 0:
        return 'stack is empty'
    else:
        deleted_value = package.pop() # .pop(0) deletes front element, .pop() deletes rear elements
        return deleted_value

package_global = list()

print(makepush(package_global, 12))

print(makepop(package_global))
# insert front
def insert_front(data, x):
    data.insert(0, x)
    return data

