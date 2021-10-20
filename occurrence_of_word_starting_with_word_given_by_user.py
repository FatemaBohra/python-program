#Question-10(FILE HANDLING)
def starting_with_word_given_by_user(file_name, word):
    file = open(file_name, 'r')
    file_line = file.readline()
    count = 0
    while file_line:
        line_list = file_line.split()
        if line_list[0] == word: 
            count = count + 1
        file_line = file.readline()
    file.close()
    return count

a = str(input('enter a word'))
print(starting_with_word_given_by_user('DATA.DAT.txt', a))