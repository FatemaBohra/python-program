# FILE HANDLING
#Question-3
def copies_upper_case_letter(file_name):
    file = open(file_name, 'r' )
    file_line = file.readline()
    s = ''
    while file_line:
        for i in range(0, len(file_line)):
            if file_line[i].isupper():
                s = s + file_line[i]
        file_line = file.readline()
    target_file = open('two.txt', 'w')
    target_file.write(s)
    file.close()
    target_file.close()

(copies_upper_case_letter('DATA.DAT.txt'))



