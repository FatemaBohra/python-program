# Question-4 (FILE HANDLING)
# I am counting each letter, so I am using file.readline() pattern in this pattern
# I will use while loop to go through each line  and inside while loop I will use for loop to gothrough each letter in that line
# parameter datatype is string , return datatype is integer
def occurrence_of_A_S(file_name):
    file = open(file_name, 'r')
    file_line = file.readline()
    count = 0
    while file_line:
        for i in range(0, len(file_line)):
            if file_line[i] == 'A' or file_line[i] == 'S':
                count = count + 1
        file_line = file.readline()
    file.close()
    return count

print(occurrence_of_A_S('DATA.DAT.txt'))