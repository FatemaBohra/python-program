# Question-9(STACK AND QUEUE)
def insertstack(stack_book, node):
    stack_book.append(node)
    return stack_book

stack_book_global = list()
node_global = {'booknumber': 12, 'bookname': 'three man in a boat'}
print(insertstack(stack_book_global, node_global))
node_global_two = {'booknumber': 1, 'bookname': 'white tiger'}
print(insertstack(stack_book_global, node_global_two))