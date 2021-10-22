# create a list whose values are of integer datatype [1, 67, 34, 6]
# whose values are string datatype  ["apple", "banana"]
# whose values are float datatype [3.14]
# it is valid to have an empty list []
# whose values are of list datatype list_in_list = [1, 2, 3, [4, 5, 6] , 4, 7, 8]
#list_in_list[0] = 1, list_in_list[3] = [4, 5, 6], list_in_list[4] = 4
# list_in_list[3][2] = 6 this called nested list
#list_in_list[4][0] *not possible becuase we can't access index of an integer
# question 3
def total_occurrence(letters, x):
    count = 0
    for i in range(0, len(letters)):
        if letters[i] == x:
           count = count + 1
    return count

a = str(input("enter  string"))
b = str(input("enter a string"))
d = total_occurrence([a, b], "a")
print(d)
