# Question-9(FILE HANDLING)
# parameter datatype is string, return datatype is string
# dealing with word so use pattern of file.read().split()
def occurrence_of_word_given_by_user(file_name, word):
    file = open(file_name, 'r')
    file_list = file.read().split()
    count = 0
    for i in range(0, len(file_list)):
        if file_list[i] == word:
            count = count + 1
    file.close()
    return count

a = str(input("enter a word"))
print(occurrence_of_word_given_by_user('DATA.DAT.txt', a))
