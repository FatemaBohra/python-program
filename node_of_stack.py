# Question-6(STACK AND QUEUE)
def makepush(data, node):# node is dictionary not integer
    data.append(node)
    return data

data_global = list()
node_global = {'pincode': 311001, 'city': 'Bhilwar'}
print(makepush(data_global, node_global))
