# Quetion-8(FILE HANDLING)
def occurrence_of_ME_MY(file_name):
    file = open(file_name, 'r')
    file_list = file.read().split()
    count = 0
    for i in range(0, len(file_list)):
        if file_list[i] == 'MY' or file_list[i] == 'ME':
            count = count + 1
    file.close()
    return count

print(occurrence_of_ME_MY('DATA.DAT.txt'))
