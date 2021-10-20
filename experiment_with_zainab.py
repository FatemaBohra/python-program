# difference between read, readline, readlines.
def read_file(file_name):
    file = open(file_name, 'r')# file variable has a local scope can't use outside the function
    print('output of file.read')# read reads the whole file, return datatype is string
    print(file.read())
    #  print('output of file.read().split()')
    #  print(file.read().split())# split() will split every word(after blank/space), return datatype is list, element datatype is string
    # print('output of file.readline')# readline reads the one line at a time, return datatype is string
    # print(file.readline())
    #  file_lines = file.readlines()
    #  print('output of file.readlines')# readlines reads the all line at a time, return datatype is list, element datatype is string every elements is in one line
    #  print(file_lines)
    # file.close()

read_file('DATA.DAT.txt')

