# question 2
def is_prime(number):
    if number == 1:# 9 != 1
        return False
    for i in range(2, number):# range = 2-4, i = 4
        if number % i == 0:# 9 % 3 == 0
            return False

    return True

a = int(input("enter a val"))
print(is_prime(a))



