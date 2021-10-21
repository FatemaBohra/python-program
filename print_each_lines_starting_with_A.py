# Question-5(FILE HANDLING)
# parameter datatype string, return datatype string
def lines_starting_with_B(file_name):
    file = open(file_name, 'r')
    file_line = file.readline()
    s = ''
    while file_line:
        if file_line[0] == 'B':
            s = s + file_line
        file_line = file.readline()
    file.close()
    return s

print(lines_starting_with_B('DATA.DAT.txt'))
