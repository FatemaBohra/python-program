# Question-2(file handling)
# parameter datatype is string, return datatype integer
def occurrence_of_this(file_name):
    count = 0
    file = open(file_name, 'r')
    file_list = file.read().split()
    for i in range(0, len(file_list)):
        if file_list[i] == 'this':
             count = count + 1
    file.close()
    return count

print(occurrence_of_this('DATA.DAT.txt'))


    #file_line = file.readline()
    # count = 0
    # while file_line:
    #     for i in range(0, len(file_line)):
    #         if file_line
