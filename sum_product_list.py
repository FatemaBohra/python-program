# question 1
def my_function(numbers):
    product = 1
    sum = 0
    for i in range(0, len(numbers)): # range of i = 0-3, i = 3,
        if numbers[i] % 2 == 0: # i = 3, numbers[3] = 5, 5 % 2 == 0
            sum = sum + numbers[i] # sum = 2 + 4 = 6
        else:
            product = product * numbers[i] # product = 3 * 5 = 15
    return sum, product # 6, 15

a = int(input("enter a value"))
b = int(input("enter a value"))
c = int(input("enter a value"))
d = int(input("enter a value"))
e = my_function([a, b, c, d])
print(e)         [2, 3, 4, 5]
(6, 15)


