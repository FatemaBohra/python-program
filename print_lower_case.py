# FILE HANDLING
#Question-1
# whenever you want to read every letter one by one use file.readline() with while loop(inside it run for loop for each letter in every line).
# file_line = file.readline() always give it at the end of  while loop(outside for loop) so it will read next line.
# whenever you want to read one word('this') at a time then use file.read().split() and use for loop to read each word at a time
def print_lower_case(file_name):
    file = open(file_name, 'r')
    file_line = file.readline()
    s = ''
    while file_line:# variable
        for i in range(0, len(file_line)):
            if file_line[i].islower():# variable
                s = s + file_line[i]
        file_line = file.readline() # store in a variable
    file.close()
    return s

print(print_lower_case('DATA.DAT.txt'))

# parameter is variable, argument is value/ parameter is variable, argument is value/ parameter is variable, argument is val

# Atribute, field, columns are same
# Tuple, rows, records are same
# number of rows is known as cardinality
# numbers of column is degree

def lower_case_letter(word):
    s = ''
    for i in range(0, len(word)):
        if word[i].islower():
            s = s + word[i]
    return s
