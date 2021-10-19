# Question-7(FILE HANDLING)
# parameter datatype is string, return datatype is string
def copy_lower_case_vowel(file_name):
    file = open(file_name, 'r')
    file_line = file.readline()
    s = ''
    while file_line:
        for i in range(0, len(file_line)):
            if file_line[i] == 'a' or file_line[i] == 'o' or file_line[i] == 'u' or file_line[i] == 'e' or file_line[i] == 'i':
                s = s + file_line[i]
        file_line = file.readline() 
    target_file = open('one.txt' , 'w')
    target_file.write(s)
    file.close()
    target_file.close()
    return s

print(copy_lower_case_vowel('DATA.DAT.txt'))

