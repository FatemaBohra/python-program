# Question-6(FILE HANDLING)
# parameter datatype is string, return datatype is string
def words_less_than_four(file_name):
    file = open(file_name, 'r')
    file_list = file.read().split()
    s = ''
    for i in range(0, len(file_list)):
        if len(file_list[i]) < 4 :
            s = s + file_list[i]
    file.close()
    return s

print(words_less_than_four('DATA.DAT.txt'))
# I access a word inside for loop by writing file_list[i]
# i access a word inside for loop by writing file_list[i]
# i access a word inside for loop by writing file_list[i]
# i access a word inside for loop by writing file_list[i]
# i access a word inside for loop by writing file_list[i]
