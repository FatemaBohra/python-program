# question 4
# parameter datatype is string, return datatype is integer
def occurrence_of_A(word):
    count = 0
    for i in range(0, len(word)): # range = 0-3, i = 0 , i = 1, i = 2, i = 3
        if word[i] == 'A': # word[3] = a
            count = count + 1 # count = 0 + 1 = 1
    return count # 1 

print(occurrence_of_A("Anna"))

thisset = {"apple", "banana"}
for x in thisset:
    print(x)


