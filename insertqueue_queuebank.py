# Question-10(STACK AND QUEUE)
def insert_queue(queue_bank, node):
    queue_bank.append(node)
    return queue_bank

queuebank_global = list()
node_global = {'custid': 201, 'custname': 'fatema'}
print(insert_queue(queuebank_global, node_global))